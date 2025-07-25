# Calculate Budget Variance:
from airflow.decorators import dag, task
from pendulum import datetime
import pandas as pd

# In dags/budget_variance_dag.py
print("DAG redeployed test")

@dag(
    schedule="@daily",
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=["budget", "finance"]
)
def budget_variance_pipeline():

    @task()
    def load_data():
        budget_df = pd.read_csv("/usr/local/airflow/include/data/budget.csv")
        actual_df = pd.read_csv("/usr/local/airflow/include/data/actual.csv")
        merged_df = budget_df.merge(actual_df, on="account")
        return merged_df.to_dict(orient="records")

    @task()
    def calculate_variance(data: list[dict]):
        df = pd.DataFrame(data)
        df["variance"] = df["actual"] - df["budget"]
        df["percent_variance"] = (df["variance"] / df["budget"]) * 100
        high_var = df[df["percent_variance"].abs() > 10]
        output_path = "/usr/local/airflow/include/data/high_variance.csv"
        high_var.to_csv(output_path, index=False)
        print(f"High variance rows saved to {output_path}")
        print(high_var)

    data = load_data()
    calculate_variance(data)

dag = budget_variance_pipeline()
