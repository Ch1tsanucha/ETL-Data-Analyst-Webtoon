from datetime import datetime,timedelta
from airflow.operators.python import PythonOperator
from airflow.decorators import dag
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.operators.dummy import DummyOperator

default_args = {
    'owner':'BB',
    'retries':5,
    'retry_delay':timedelta(minutes=5)
}

@dag(
    dag_id='dag_etl_01',
    default_args=default_args,
    start_date=datetime(2024, 10, 1),
    schedule_interval='@monthly',
    catchup=True
)
def dag_start():
    
    run_docker_container_E01 = DockerOperator(
    task_id='run_extract_container_E1',
    docker_url="tcp://docker-socket-proxy:2375",
    image='etl', 
    api_version='auto',
    auto_remove=False,
    command='python extract.py 0 9',
     mounts=[
        {
            "source": "app_data",
            "target": "/app",
            "type": "volume", 
        }
    ], 


)

    run_docker_container_E02 = DockerOperator(
    task_id='run_extract_container_E2',
    docker_url="tcp://docker-socket-proxy:2375",
    image='etl', 
    api_version='auto',
    auto_remove=False,
    command='python extract.py 1 8',
     mounts=[
        {
            "source": "app_data",
            "target": "/app",
            "type": "volume", 
        }
    ], 

)

    run_docker_container_E03 = DockerOperator(
    task_id='run_extract_container_E3',
    docker_url="tcp://docker-socket-proxy:2375",
    image='etl', 
    api_version='auto',
    auto_remove=False,
    command='python extract.py 2 7',
     mounts=[
        {
            "source": "app_data",
            "target": "/app",
            "type": "volume", 
        }
    ], 
   

)

    run_docker_container_E04 = DockerOperator(
    task_id='run_extract_container_E4',
    docker_url="tcp://docker-socket-proxy:2375",
    image='etl', 
    api_version='auto',
    auto_remove=False,
    command='python extract.py 3 6',
     mounts=[
        {
            "source": "app_data",
            "target": "/app",
            "type": "volume",  
        }
    ], 


)

    run_docker_container_E05 = DockerOperator(
    task_id='run_extract_container_E5',
    docker_url="tcp://docker-socket-proxy:2375",
    image='etl',
    api_version='auto',
    auto_remove=False,
    command='python extract.py 4 5',
     mounts=[
        {
            "source": "app_data",
            "target": "/app",
            "type": "volume",  
        }
    ], 


)

    run_docker_container_E06 = DockerOperator(
    task_id='run_extract_container_E6',
    docker_url="tcp://docker-socket-proxy:2375",
    image='etl', 
    api_version='auto',
    auto_remove=False,
    command='python extract.py 5 4',
     mounts=[
        {
            "source": "app_data",
            "target": "/app",
            "type": "volume", 
        }
    ], 


)

    run_docker_container_E07 = DockerOperator(
    task_id='run_extract_container_E7',
    docker_url="tcp://docker-socket-proxy:2375",
    image='etl',
    api_version='auto',
    auto_remove=False,
    command='python extract.py 6 3',
     mounts=[
        {
            "source": "app_data",
            "target": "/app",
            "type": "volume", 
        }
    ], 
 

)

    run_docker_container_E08 = DockerOperator(
    task_id='run_extract_container_E8',
    docker_url="tcp://docker-socket-proxy:2375",
    image='etl', 
    api_version='auto',
    auto_remove=False,
    command='python extract.py 7 2',
     mounts=[
        {
            "source": "app_data",
            "target": "/app",
            "type": "volume",
        }
    ], 


)

    run_docker_container_E09 = DockerOperator(
    task_id='run_extract_container_E9',
    docker_url="tcp://docker-socket-proxy:2375",
    image='etl',
    api_version='auto',
    auto_remove=False,
    command='python extract.py 8 1',
     mounts=[
        {
            "source": "app_data",
            "target": "/app",
            "type": "volume", 
        }
    ], 
    
)

    run_docker_container_E10 = DockerOperator(
    task_id='run_extract_container_E10',
    docker_url="tcp://docker-socket-proxy:2375",
    image='etl', 
    api_version='auto',
    auto_remove=False,
    command='python extract.py 9 0',
     mounts=[
        {
            "source": "app_data",
            "target": "/app",
            "type": "volume",
        }
    ], 

)

    run_docker_container_CONCAT = DockerOperator(
    task_id='run_concat_container_C1',
    docker_url="tcp://docker-socket-proxy:2375",
    image='etl',
    api_version='auto',
    auto_remove=False,
    command='python concat.py',
     mounts=[
        {
            "source": "app_data",
            "target": "/app",
            "type": "volume",
        }
    ], 

)

    
    run_docker_container_T01 = DockerOperator(
    task_id='run_transform_container_T',
    docker_url="tcp://docker-socket-proxy:2375",
    image='etl',
    api_version='auto',
    auto_remove=False,
    command='python transform.py',
     mounts=[
        {
            "source": "app_data",
            "target": "/app",
            "type": "volume",
        }
    ], 
    
)
    
    run_docker_container_L01 = DockerOperator(
    task_id='run_load_container_L',
    docker_url="tcp://docker-socket-proxy:2375",
    image='etl', 
    api_version='auto',
    auto_remove=False,
    command='python load.py',
     mounts=[
        {
            "source": "app_data",
            "target": "/app",
            "type": "volume",  
        }
    ], 
    network_mode = 'airflow_default',
)

    
    wait1 = DummyOperator(task_id='merge1')
    wait2 = DummyOperator(task_id='merge2')

    [run_docker_container_E01,run_docker_container_E02,run_docker_container_E03,run_docker_container_E04,run_docker_container_E05] >> \
    wait1 >> \
    [run_docker_container_E06,run_docker_container_E07,run_docker_container_E08,run_docker_container_E09,run_docker_container_E10,] >> \
    wait2 >> \
    run_docker_container_CONCAT >>run_docker_container_T01 >> run_docker_container_L01

dag_instance = dag_start()
