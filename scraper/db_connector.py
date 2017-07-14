import json
import boto3
from boto3.dynamodb.conditions import Key, Attr

class database_connector:
    def __init__(self, table_name, region_name):
        self.table_name = table_name
        self.region_name = region_name

    def init_db(self):
        self.dynamodb = boto3.resource('dynamodb', region_name=self.region_name)
        self.table = self.dynamodb.Table(self.table_name)
        print(self.table)

    def add(self, item):
        self.table.put_item(Item=item)
        
    # def create_table(self):
    #     self.table = self.create_table(
    #         TableName = self.table_name,
    #         KeySchema = [
    #             {

    #             }
    #         ]
    #     )

        # self.table = self.dynamodb.create_table(
        #     TableName=self.table_name,
        #     KeySchema=[
        #         {
        #             'AttributeName': 'person',
        #             'KeyType': 'HASH'  #Partition key
        #         },
        #         {
        #             'AttributeName': 'event',
        #             'KeyType': 'RANGE'  #Sort key
        #         },
        #         {
        #             'AttributeName': 'brand',
        #             'KeyType': 'RANGE'  #Sort key
        #         },
        #         {
        #             'AttributeName': 'image_url',
        #             'KeyType': 'RANGE'  #Sort key
        #         }
        #     ],
        #     AttributeDefinitions=[
        #         {
        #             'AttributeName': 'year',
        #             'AttributeType': 'N'
        #         },
        #         {
        #             'AttributeName': 'title',
        #             'AttributeType': 'S'
        #         },

        #     ],
        #     ProvisionedThroughput={
        #         'ReadCapacityUnits': 10,
        #         'WriteCapacityUnits': 10
        #     }
        # )

        # print("Table status:", self.table.table_status)

# def import_data(json_file, db_table_name):
#     dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
#     table = dynamodb.Table(db_table_name)

# data_scraper = database_connector("RedCarpet", "us-east-1")
# data_scraper.init_db()