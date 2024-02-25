import json
import boto3

s3_client = boto3.client('s3')
dy_dyn = boto3.resource('dynamodb')


def lambda_handler(event, context):
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_name = event['Records'][0]['s3']['object']['key']

    json_object = s3_client.get_object(Bucket=bucket_name, Key=file_name)
    json_read = json_object['Body'].read()

    json_dict = json.loads(json_read)
    table = dy_dyn.Table('customers')

    for line in json_dict:
        table.put_item(Item=line)

    return "hello"
