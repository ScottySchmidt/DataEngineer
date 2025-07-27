from airflow.decorators import dag, task
from airflow.providers.amazon.aws.operators.glue import GlueJobOperator
from airflow.providers.amazon.aws.transfers.s3_to_redshift import S3ToRedshiftOperator
from airflow.providers.amazon.aws.operators.s3 import S3CreateObjectOperator
from airflow.providers.amazon.aws.hooks.base_aws import AwsBaseHook
from airflow.utils.dates import days_ago
import requests
import json

@dag(
    schedule_interval='@daily',
    start_date=days_ago(1),
    catchup=False,
    tags=['aws', 's3', 'glue', 'redshift'],
)
def daily_sales_pipeline():

    @task()
    def fetch_sales_data():
        response = requests.get("https://api.example.com/sales")
        data = response.json()
        # Save locally for upload
        with open('/tmp/sales.json', 'w') as f:
            json.dump(data, f)
        return '/tmp/sales.json'

    @task()
    def upload_to_s3(file_path: str):
        hook = AwsBaseHook(aws_conn_id='aws_default', client_type='s3')
        s3 = hook.get_client_type('s3')
        bucket = "my-sales-raw-data"
        key = "daily/sales.json"
        s3.upload_file(file_path, bucket, key)
        return f"s3://{bucket}/{key}"

    run_glue_etl = GlueJobOperator(
        task_id='run_glue_etl',
        job_name='sales_etl_job',
        script_location='s3://my-glue-scripts/sales_etl.py',
        aws_conn_id='aws_default',
        region_name='us-east-1',
    )

    load_to_redshift = S3ToRedshiftOperator(
        task_id='load_to_redshift',
        schema='public',
        table='sales',
        s3_bucket='my-sales-processed-data',
        s3_key='daily/cleaned_sales.parquet',
        copy_options=['FORMAT AS PARQUET'],
        method='REPLACE',
        redshift_conn_id='redshift_default',
        aws_conn_id='aws_default'
    )

    # DAG flow
    path = fetch_sales_data()
    s3_uri = upload_to_s3(path)
    run_glue_etl >> load_to_redshift

dag = daily_sales_pipeline()
