import boto3
import json
dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000', region_name= 'eu-west-2')
table= dynamodb.Table('zacresumetable2')
os.environ["AWS_ACCESS_KEY_ID"] = "test"
os.environ["AWS_SECRET_ACCESS_KEY"] = "test"

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
