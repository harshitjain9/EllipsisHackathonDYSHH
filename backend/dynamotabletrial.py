# import boto3 module
import boto3
import os

os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'
os.environ['AWS_ACCESS_KEY_ID'] = 'ASIA23U5KVIYHD24DGWK'
os.environ['AWS_SECRET_ACCESS_KEY'] = '+noCVI5Vzm1DwuMeK+619MfsrpxvfadTcQw4uXSt'

# Generating a resources from the default session
dynamodb = boto3.resource('dynamodb')

def create_table():
    """
    This function creates a table in dynamodb
    Returns
    -------
    String
        table creation status string
    """
    table = dynamodb.create_table(
        TableName='mytable',
        KeySchema=[ 
            {
                'AttributeName': 'username',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'password',
                'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'user_email',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'password',
                'AttributeType': 'S'
            }
         ],
         ProvisionedThroughput={
             'ReadCapacityUnits': 1,
             'WriteCapacityUnits': 1
         }
    )
    return table.table_status

def insert_data():
    """
    This function inserts data in dynamodb table
    Returns
    -------
    Dictionary
        Response Dictionary
    """
    table = dynamodb.Table('user_credentials') 
    #with put_item function we insert data in Table
    response = table.put_item(
        Item = {
               'username': 'aastha@gmail.com',
               'password': 'password',
               'first_name':'Aastha'  
               } 
        )
    return response

insert_data()