from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
import re
from html.parser import HTMLParser

# Helper methods
from helpers import remove_tags, remove_extra

class RedCarpetScraper:
    mBaseURL = "http://www.eonline.com"
    mRedCarpetMenuURL = "/news/red_carpet"
    mEventURLs = {}
    mEvents = {}
    decoder = HTMLParser()
    
    def __init__(self, db):
        self.db = db

    def getMenus(self):
        # Open the Red Carpet menu
        # Currently issues behind a corporate firewall
        redCarpetMenuHTML = urlopen(self.mBaseURL)
        # Get the HTML
        soup = BeautifulSoup(redCarpetMenuHTML.read(), "lxml")
        # find all menu items and iterate over the menu items
        menus = soup.findAll('li', { "class": "nav__menu-item" })
        for menuItem in menus:
            # Find the Red Carpet menu
            if "RED CARPET" in menuItem.text:
                # Populate all the event menus
                submenuItems = (menuItem.find_all('a', href=True))
                for submenuItem in submenuItems:
                    self.mEventURLs[submenuItem.text] = submenuItem['href'] + "/photos"
                break # Once we find the Red Carpet menu we can stop
        self.mEventURLs.pop("RED CARPET")

        
    def getEvents(self):
        for key, value in self.mEventURLs.items():
            self.getEvent(value)

    def getEvent(self, url):
        # print("GETTING ", url)
        matchTerm = "red carpet arrivals"
        link = urlopen(url)
        html = BeautifulSoup(link.read(), "lxml")
        galeryGrid = html.find('div', { "id": "category-news-list-1" })
        galeries = galeryGrid.find_all('a')
        for galerryItem in galeries:
            if matchTerm.lower() in galerryItem.text.lower():
                pos = galerryItem.text.lower().find(matchTerm)
                showName = galerryItem.text[:pos]
                self.mEvents[showName.strip()] = self.mBaseURL + galerryItem['href']

    def getRedCarpetArrivals(self):
        for key, value in self.mEventURLs.items():
            self.getRedCarpetArrival(value)

    def getRedCarpetArrival(self, url):
        link = urlopen(url)
        html = BeautifulSoup(link.read(), "lxml")
        galleries = html.find("ul", {"id": "gallery-list1", "class": "category-gallery-list clear"})
        for gallery in galleries:
            if gallery.find('span') is not -1:
                if "arrivals" in gallery.find('span').text.lower():
                    galleryURL = self.mBaseURL + gallery.find('a', href=True)['href']
                    self.getGallery(galleryURL)
                    break
            # break # Remove

    # Inspects the source of the webpage to get the script data and get the json response
    def getGallery(self, url):
        link = urlopen(url)
        html = link.read()
        res = BeautifulSoup(html, "lxml")
        scripts = res.find_all('script')
        for script in scripts:
            if r"window.HHCAROUSEL_DATA" in str(script):
                s = script.text
                start = s.find(r"window.HHCAROUSEL_DATA")
                end = s.find(r" //end of HHCAROUSEL_DATA")
                wholeObj = s[start + len(r"window.HHCAROUSEL_DATA = "):end]
                imagesBegin = wholeObj.find(r"images: ")
                rawData = wholeObj[imagesBegin + len(r"images: "):-4]
                rawData = rawData.replace(r"'", r'"')
                jsonData = json.loads(rawData)
                title = self.getFullTitle(s)
                title = title.replace("\\", r'').replace(r':', r'')
                print(title)
                title = ("".join([c for c in title if not c.isdigit()])).strip()
                print(title)
                print("DATA")
                for eventItem in jsonData:
                    brand = eventItem['description']
                    brand = remove_tags(brand)
                    if "&nbsp;" in brand:
                        brand = ""
                    brand = self.decoder.unescape(brand)
                    # brand = remove_extra(brand)
                    item = {
                        "person": eventItem["title"],
                        "event": title,
                        "brand": brand,
                        "image_url": eventItem["url"]
                    }
                    self.db(item)
                break

    def getFullTitle(self, tagData):
        selectTitlePattern = r'title: "(.*)"'
        title = re.search(selectTitlePattern, tagData)
        title = title.group(1)
        title = title.replace("Red Carpet Arrivals", "").lstrip()
        return title

    def printURLS(self):
        for key, value in self.mEventURLs.items():
            print(key, value)

        print("Show list")
        for key, value in self.mEvents.items():
            print(key, value)

    def run(self):
        self.getMenus()
        self.getEvents()
        self.getRedCarpetArrivals()