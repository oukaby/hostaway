from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime
import os


# Define the absolute path for DBT directory
dbt_project_path = os.path.abspath('./dbt')

# Define the DAG
with DAG(
    'sales_data_ingestion_dag',
    default_args={
        'owner': 'airflow',
        'retries': 1,
    },
    description='A DAG to ingest, process, and load sales data into PostgreSQL',
    schedule_interval=None,  # Can be set to a cron expression to schedule the DAG
    start_date=datetime(2023, 1, 1),
    catchup=False,
) as dag:

    # Step 1: Ingest and process the CSV file
    process_data_task = BashOperator(
        task_id='process_data',
        bash_command='python /opt/airflow/python/scripts/ingest_and_process_data.py',
        dag=dag
    )

    # Step 2: Load processed data into PostgreSQL
    load_data_task = BashOperator(
        task_id='load_data_to_postgres',
        bash_command='python /opt/airflow/python/scripts/load_data_to_postgres.py',
        dag=dag
    )

    # Step 3: Define the task to run DBT
    dbt_task = DockerOperator(
        task_id='dbt_task',
        image='interview-data-engineer-dbt:latest',
        api_version='auto',
        command='dbt build',
        docker_url='unix://var/run/docker.sock',
        network_mode='interview-data-engineer_airflow-db-network',
        working_dir='/opt/airflow/dbt',
        dag=dag,
    )

    # Task dependencies
    process_data_task >> load_data_task >> dbt_task