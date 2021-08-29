# import boto3 module
import boto3
import os

#os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'
#os.environ['AWS_ACCESS_KEY_ID'] = 'JASIA2FSXXOSNOYM6O6VW'
#os.environ['AWS_SECRET_ACCESS_KEY'] = 'JgBptKPrlMOel6cslDO+v7kEbAHlRLONC75jwIVV'
#os.environ['AWS_SESSION_TOKEN'] = 'FwoGZXIvYXdzEHcaDBdPJwdmrhN/gbAHCiLSAdyEf92NHD13wYoJ86gNEP7UoRrqh5Vv7E1uhmZBRluU0EtTIbcWz5t7oHHDA+gZ++9DmwiQTOfc62JD8tszEoq+MmbBdMYidz9z2CHygKf7kcQ86CjpXpgqo9mH11HgmIcnQIoPIDaQ+7Xnot260dks0YcmT5fzHIcd8ucRw9EFw7HN5E4mqSoG9sqHXmyRPBTCGXeU875D8f+Kpx6U+8dGbXXKugYEoSaJSdg6Nuajue9lJ2nSA2k3kiIpecbd2AYn/1KNxWgxYBYb8WkIVqjpOSj0xKyJBjItQbdZMWzycueUKkpKNHD6OyhBVzomwmi6vkYvli2Ehfoe08NWTiIBaF51fKkN'

# Generating a resources from the default session
dynamodb = boto3.resource('dynamodb')
#print(boto3.client('sts').get_caller_identity())
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
                'AttributeName': 'username',
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
create_table()
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