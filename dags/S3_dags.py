# connecting to AWS S3
from airflow.decorators import dag, task
from pendulum import datetime
import boto3

@dag(schedule="@daily", start_date=datetime(2025,1,1), catchup=False)
def s3_upload_example():
    
    @task
    def upload_to_s3():
        s3 = boto3.client('s3', region_name="us-east-1")
        bucket_name = "my-data-bucket-123-scotty"
        s3.upload_file("local_file.csv", bucket_name, "uploads/local_file.csv")
        return "Uploaded successfully"

    upload_to_s3()

dag = s3_upload_example()
