from airflow import DAG
from airflow.providers.amazon.aws.operators.lambda_function import LambdaInvokeOperator
from airflow.utils.dates import days_ago

# Define the DAG
dag = DAG(
    'lambda_trigger_example',
    schedule_interval='@daily',
    start_date=days_ago(1),
    catchup=False
)

# Task to invoke Lambda function
invoke_lambda = LambdaInvokeOperator(
    task_id='invoke_lambda_task',
    function_name='your_lambda_function_name',
    aws_conn_id='aws_default',  # Your AWS connection id in Airflow
    log_type='Tail',  # Optional: To get logs
    payload='{}',  # Optional: Pass any payload if required by the Lambda
    region_name='us-east-1',  # Region where your Lambda is deployed
    dag=dag
)

invoke_lambda
