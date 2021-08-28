# import boto3 module
import boto3
import os

#os.environ['AWS_DEFAULT_REGION'] = ''
#os.environ['AWS_ACCESS_KEY_ID'] = ''
#os.environ['AWS_SECRET_ACCESS_KEY'] = ''

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

def get_data():
    """
    This function reads data from dynamodb table
    Returns
    -------
    
        Response Dictionary
    """
    table = dynamodb.Table('mytable')
    #with Get_item function we get the data
    response = table.get_item(
        Item = {
               'username': 'aastha@gmail.com',
               'password':'password'
               }
        )
    return response['Item']


def delete_data():
    """
    This function delete data from dynamodb table
    Returns
    -------
    
        Response Dictionary
    """
    table = dynamodb.Table('mytable')
    #with delete_item function we delete the data from table
    response = table.delete_item(
        Item = {
               'username': 'aastha@gmail.com',
               'password':'password'
               }
        )
    return response['Item']

def update_data():
    """
    This function delete data from dynamodb table
    Returns
    -------
    
        Response Dictionary
    """
    table = dynamodb.Table('mytable')
    #with delete_item function we delete the data from table
    response = table.update_item(
                Key={
                    'username':'aastha@gmail.com',
                    'password': 'password'
                    },
                UpdateExpression='SET fname = :values',
                ExpressionAttributeValues={
                    ':values': 'Aastha Gupta'
                }
           )
    return response['Item']


#insert_data()