import pytest
import boto3
import json
dynamodb = boto3.resource('dynamodb', region_name= 'eu-west-2')
table= dynamodb.Table('zacresumetable2')

def lambda_handler(test_event, test_context):
    def test_event:
    assert True
    def test_context:
    assert 1 == 1
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
