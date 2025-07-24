from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import duckdb

def create_galaxy_table():
    conn = duckdb.connect('include/astronomy.db')
    conn.execute("""
        CREATE TABLE IF NOT EXISTS galaxies (
            id INTEGER,
            name TEXT,
            type TEXT,
            distance FLOAT
        );
    """)
    conn.close()

with DAG(
    dag_id="create_galaxy_table_dag",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False
) as dag:

    create_table = PythonOperator(
        task_id="create_galaxy_table",
        python_callable=create_galaxy_table
    )
