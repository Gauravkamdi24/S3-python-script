import boto3
s3_client=boto3.client('s3')
res=s3_client.create_bucket (
    Bucket='Jubli-project',

)