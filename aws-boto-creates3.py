
import boto3
sess = boto3.Session(region_name='us-west-2')
s3client = sess.client('s3')

bucket_name = 'bucket-boto3-rohit-276'

s3_location = {
    'LocationConstraint': 'us-west-2'
}

s3client.create_bucket(Bucket=bucket_name,CreateBucketConfiguration=s3_location)

