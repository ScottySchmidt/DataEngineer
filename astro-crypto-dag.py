from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import requests
import pandas as pd

def fetch_coingecko_data():
    url = 'https://api.coingecko.com/api/v3/coins/markets'
    params = {
        'vs_currency': 'usd',
        'order': 'market_cap_desc',
        'per_page': 10,
        'page': 1,
        'sparkline': 'false'
    }
    response = requests.get(url, params=params)
    data = response.json()
    df = pd.DataFrame(data)
    df = df[['id', 'symbol', 'current_price', 'market_cap']]
    df.to_csv('/tmp/crypto_data.csv', index=False)
    print("Saved crypto_data.csv!")

with DAG('coingecko_dag',
         start_date=datetime(2024, 1, 1),
         schedule_interval='@daily',
         catchup=False) as dag:

    task = PythonOperator(
        task_id='fetch_and_save_crypto_data',
        python_callable=fetch_coingecko_data
    )
