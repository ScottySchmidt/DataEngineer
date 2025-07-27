from airflow.decorators import dag, task
from pendulum import datetime

@dag(schedule="@daily", start_date=datetime(2024, 1, 1), catchup=False)
def my_pipeline():
    @task
    def pull_data():
        return "data pulled"

    @task
    def process(data):
        return f" {data} processed"

    process(pull_data())

dag = my_pipeline()
