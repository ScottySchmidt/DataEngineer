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

    # Chain everything together
    path = fetch_sales_data()
    s3_uri = upload_to_s3(path)

    # Now wrap operators inside a Python function so you can call them dynamically
    @task()
    def run_glue():
        return GlueJobOperator(
            task_id='run_glue_etl',
            job_name='sales_etl_job',
            script_location='s3://my-glue-scripts/sales_etl.py',
            aws_conn_id='aws_default',
            region_name='us-east-1',
        ).execute({})  # Needed for manual operator call inside task

    @task()
    def load_redshift():
        return S3ToRedshiftOperator(
            task_id='load_to_redshift',
            schema='public',
            table='sales',
            s3_bucket='my-sales-processed-data',
            s3_key='daily/cleaned_sales.parquet',
            copy_options=['FORMAT AS PARQUET'],
            method='REPLACE',
            redshift_conn_id='redshift_default',
            aws_conn_id='aws_default'
        ).execute({})

    glue = run_glue()
    redshift = load_redshift()
    glue >> redshift

dag = daily_sales_pipeline()
