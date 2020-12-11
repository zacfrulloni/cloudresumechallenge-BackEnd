import boto3
import json
region = 'eu-west-2'
dynamodb = boto3.resource('dynamodb')
table= dynamodb.Table('zacresumetable2')

def lambda_handler(event, context):
    response= table.update_item(
    Key= {'URL': 'zacresume.com'},
    UpdateExpression= "SET visits = visits + :increase",
    ExpressionAttributeValues= {':increase': 1},
    ReturnValues= "UPDATED_NEW"
)
    return {'statusCode': 200,
            'body': json.dumps('visitsUpdated'),
            'headers': {'Content-Type': 'application/json'}}
print("UPDATING ITEM")
print("response") 