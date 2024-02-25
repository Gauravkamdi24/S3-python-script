import boto3
s3_client=boto3.client('s3')
res=s3_client.delete_object(
    Bucket='myfirstbucketbypycham',
    Key='shyamwebpage.html',
)
s3_client=boto3.client('s3')
resp=s3_client.delete_bucket(
    Bucket='myfirstbucketbypycham',
    ExpectedBucketOwner='077829623500',
)
