from airflow.decorators import dag, task
from pendulum import datetime

@dag(schedule="@daily", start_date=datetime(2024, 1, 1), catchup=False, tags=["weather"])
def weather_pipeline():

    @task()
    def fetch_weather_data():
        print("Pretend we’re calling a weather API")
        return {"temp": 72, "humidity": 50}

    @task()
    def clean_data(data):
        print("Cleaning the weather data")
        return {"temp": data["temp"], "humidity": data["humidity"]}

    @task()
    def load_to_db(data):
        print(f"Uploading to database: {data}")
        # In reality you'd connect to Postgres, BigQuery, etc.

    raw = fetch_weather_data()
    cleaned = clean_data(raw)
    load_to_db(cleaned)

dag = weather_pipeline()
