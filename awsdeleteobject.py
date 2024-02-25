import boto3
s3_client=boto3.client('s3')
res=s3_client.delete_object(
    Bucket='myfirstbucketbypycham',
    Key='datapipeline.json',
)
