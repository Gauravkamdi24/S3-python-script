import boto3
s3_client = boto3.client('s3')
response = s3_client.create_bucket(
    Bucket='myfirstbucketbypycham',
)

s3 = boto3.client('s3')
s3.upload_file('C:/Users/MORAYA/Documents/shyamwebpage.html','myfirstbucketbypycham','shyamwebpage.html')
