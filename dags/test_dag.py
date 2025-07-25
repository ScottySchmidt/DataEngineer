from airflow.decorators import dag, task
from pendulum import datetime

@dag(schedule="@daily", start_date=datetime(2024, 1, 1), catchup=False)
def example_pipeline():

    @task()
    def get_data():
        return {"a": 5, "b": 10}

    @task()
    def process_data(data):
        return data["a"] + data["b"]

    raw = get_data()
    result = process_data(raw)

dag = example_pipeline()
