# AWS S3
'''This folder contains S3-related configurations, scripts, and notes.
- Bucket policies
- S3 event triggers
- Data sync configs
'''

import boto3

s3 = boto3.client('s3')
bucket_name = "scott-data-redshift-test"
file_path = "retail_sales.csv"
s3_key = "raw/retail_sales.csv"

s3.upload_file(file_path, bucket_name, s3_key)
print(f"Uploaded {file_path} to s3://{bucket_name}/{s3_key}")
