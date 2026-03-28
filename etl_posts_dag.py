from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="etl_posts_pipeline",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    transform_csv = BashOperator(
        task_id="transform_literacy_csv",
        bash_command="python /root/airflow_project/scripts/transform/transform_literacy_csv.py",
    )

    transform_csv
from datetime import datetime

with DAG(
    dag_id="etl_posts_pipeline",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    extract = BashOperator(
        task_id="extract_posts",
        bash_command="python /root/airflow_project/scripts/extract/extract_posts.py",
    )

    transform = BashOperator(
        task_id="transform_posts",
        bash_command="python /root/airflow_project/scripts/transform/transform_posts.py",
    )

    load = BashOperator(
        task_id="load_posts",
        bash_command="python /root/airflow_project/scripts/load/load_posts.py",
    )

    extract >> transform >> load
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="etl_posts_pipeline",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    extract = BashOperator(
        task_id="extract_posts",
        bash_command="python /root/airflow_project/scripts/extract/extract_posts.py",
    )

    extrac