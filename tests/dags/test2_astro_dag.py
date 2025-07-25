# Originally from github should save onto astro cloud
from airflow.decorators import dag, task
from pendulum import datetime
import os

@dag(
    schedule="@once",  # Runs only when manually triggered
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=["astro", "test"]
)
def test_astro_dag():

    @task()
    def log_and_save():
        message = "✅ Hello from Astro Cloud!"
        print(message)

        # Save to a file in Astro's Airflow environment
        output_path = "/usr/local/airflow/include/data/astro_hello.txt"
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w") as f:
            f.write(message)
        print(f"Saved message to {output_path}")

    log_and_save()

dag = test_astro_dag()
