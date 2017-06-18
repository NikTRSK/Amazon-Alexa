#import requests
# import html from lxml
from urllib.request import urlopen
from bs4 import BeautifulSoup

class RedCarpetScraper:
    mBaseURL = "http://www.eonline.com"
    mRedCarpetMenuURL = "/news/red_carpet"
    mEventURLs = {}
    mEvents = {}
    
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
        print("GETTING ", url)
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

    # Inspects the source of the webpage to get the script data and get the json response
    def getGallery(self, url):
        import re
        link = urlopen(url)
        # html = BeautifulSoup(link.read(), "lxml")
        # print(html.prettify().encode("utf-8"))
        f = open('text.txt', 'w')
        html = link.read()
        res = BeautifulSoup(html, "lxml")
        # f.write(html)
        # f.write(res.find_all('script'))
        # print(res.script.images)
        # f.write(res.encode("utf-8"))
        results = res.find_all('script')
        # pattern = re.compile('images: \[\s+(.*\s)+};')
        regex = r"images: \[\s+(.*\s)+};"
        # t = pattern.findall(str(res))
        # print(t)
        for script in results:
            if r"window.HHCAROUSEL_DATA" in str(script):
                # print(script)
                print(type(script.text))
                s = script.text
                start = s.find(r"window.HHCAROUSEL_DATA")
                end = s.find(r" //end of HHCAROUSEL_DATA")
                f.write(s[start:end])
                break

    def printURLS(self):
        for key, value in self.mEventURLs.items():
            print(key, value)

        print("Show list")
        for key, value in self.mEvents.items():
            print(key, value)

scraper = RedCarpetScraper()
# scraper.getMenus()
# scraper.getEvents()
# scraper.printURLS()
tempURL = "http://www.eonline.com/photos/20157/oscars-2017-red-carpet-arrivals/745952"
temoURLSource = "view-source:http://www.eonline.com/photos/20157/oscars-2017-red-carpet-arrivals/745952"
scraper.getGallery(tempURL)