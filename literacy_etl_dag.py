from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

# Email alert configuration
default_args = {
    "owner": "airflow",
    "email": ["youremail@gmail.com"],   # replace with your email
    "email_on_failure": True,
    "email_on_retry": False,
}

with DAG(
    dag_id="literacy_csv_etl_pipeline",
    default_args=default_args,
    start_date=datetime(2025,1,1),
    schedule="@daily",
    catchup=False,
) as dag:

    extract = BashOperator(
        task_id="extract_literacy_csv",
        bash_command="python3 /root/airflow_project/scripts/extract/extract_literacy_csv.py",
        retries=2,
    )

    transform = BashOperator(
        task_id="transform_literacy_csv",
        bash_command="python3 /root/airflow_project/scripts/transform/transform_literacy_csv.py",
        retries=2,
    )

    load = BashOperator(
        task_id="load_literacy_csv",
        bash_command="python3 /root/airflow_project/scripts/transform/load_literacy_csv.py",
        retries=2,
    )

    extract >> transform >> load