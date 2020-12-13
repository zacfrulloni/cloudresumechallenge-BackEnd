import boto3
import json
dynamodb = boto3.resource('dynamodb', aws_access_key_id= 'ACCESS_ID', aws_secret_access_key= 'ACCESS_KEY', endpoint_url= "https://s3-eu-west-2.amazonaws.com", region_name= 'eu-west-2')
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
print(list(dynamodb.tables.all()))

