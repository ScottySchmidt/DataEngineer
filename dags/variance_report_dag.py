@task()
def read_actual_and_budget():
    base = os.path.join(os.environ["AIRFLOW_HOME"], "include", "data")
    actual_df = pd.read_csv(os.path.join(base, "actual.csv"))
    budget_df = pd.read_csv(os.path.join(base, "budget.csv"))
    
    merged = actual_df.merge(budget_df, on=["department", "category"], suffixes=("_actual", "_budget"))
    merged["variance"] = merged["amount_actual"] - merged["amount_budget"]
    print(merged)
