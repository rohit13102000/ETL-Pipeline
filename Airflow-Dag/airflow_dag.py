from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'Pratik & Rohit',
    'start_date': datetime(2025, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    dag_id='ETL_Pipeline',
    default_args=default_args,
    schedule_interval='0 0 * * *',  # Daily at 12 AM
    catchup=False,
    description='A daily Running Pipeline scheduled daily at midnight'
)
# Data Extraction 
task1 = BashOperator(
    task_id='Data_Extract',
    bash_command='bash -c "/home/talentum/ProjectDBDA/data_ingest/hadoop_ingest.sh"',
    retries=0,
    dag=dag
)
# Data Transformation and Load
task2 = BashOperator(
    task_id='Data_Transformation_and_Load',
    bash_command='python3 /home/talentum/ProjectDBDA/notebook.py',
    retries=0,
    dag=dag
)
#Data Clear
task3 = BashOperator(
    task_id='Hadoop_Data_Clear',
    bash_command='bash -c "/home/talentum/ProjectDBDA/hadoop_clear.sh"',
    dag=dag
)
#Data Export
task4=BashOperator(
	task_id='Export_From_Hive',
	bash_command="hive -f /home/talentum/ProjectDBDA/csv_export.hive",
	dag=dag
)
task1>>task2>>task3>>task4

