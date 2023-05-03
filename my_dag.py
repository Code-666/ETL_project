from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

import extract, transform, load

with DAG("my_dag", start_date=datetime(2023, 5, 3),
         schedule_interval='@daily', catchup=False) as dag:

    Extract = PythonOperator(
        task_id="Extract",
        python_callable=extract
    )

    Transform = PythonOperator(
        task_id="Transform",
        python_callable=transform
    )

    Load = PythonOperator(
        task_id="Load",
        python_callable=load
    )

    Extract >> Transform >> Load
