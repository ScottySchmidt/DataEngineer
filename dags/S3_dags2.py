# s3_dag2.py
# Start simple: connecting Airflow to AWS S3

from airflow.decorators import dag, task
from pendulum import datetime
import boto3
import os

@dag(schedule="@daily", start_date=datetime(2025,1,1), catchup=False, tags=["s3"])
def s3_upload_example():
    
    @task
    def upload_to_s3():
        bucket_name = "my-data-bucket-123-scotty"
        local_file = "local_file.csv"
        object_key = "uploads/local_file.csv"
        
        if not os.path.exists(local_file):
            raise FileNotFoundError(f"Local file not found: {local_file}")

        s3 = boto3.client('s3', region_name="us-east-1")
        
        try:
            s3.upload_file(local_file, bucket_name, object_key)
            print(f"Uploaded {local_file} to s3://{bucket_name}/{object_key}")
            return "Upload successful"
        except Exception as e:
            print(f"Upload failed: {e}")
            raise

    upload_to_s3()

dag = s3_upload_example()
