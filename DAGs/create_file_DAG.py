from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import subprocess

def run_python_script():
    subprocess.run(['python', '/home/cees/DBT/project1_semantic_thing/main/write_json.py'], capture_output=True, text=True)


with DAG(
    '01-Run-This-Dag',
    description='A DAG to run a Python script',
    schedule_interval='@daily',  
    start_date=datetime(2023, 1, 1),  
    catchup=False  
) as dag:

    run_script_task = PythonOperator(
        task_id='run_python_script',
        python_callable=run_python_script
    )

run_script_task
