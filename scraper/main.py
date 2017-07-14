from db_connector import database_connector
from redcarpetscraper import RedCarpetScraper

def __main__():
    # Init and connect to DynamoDB database
    db = database_connector("RedCarpet", "us-east-1")
    db.init_db()

    # Init scraper
    scraper = RedCarpetScraper(db)
    scraper.run()

if __name__ == "__main__":
    __main__()