from airflow import Dataset
from airflow.decorators import dag, task
from pendulum import datetime
import os
import sys

#Path de carpeta
path_dag = os.path.dirname(os.path.dirname(__file__))
path_prueba = os.path.join(path_dag,"src","scrapingTrabajo")
sys.path.append(path_prueba)


path_prueba = os.path.join(path_prueba,"prueba")
sys.path.append(path_prueba)

print(sys.path)

from prueba.prueba_main import main


# Definir el DAG
@dag(
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
)
def prueba_actualizacion_dags_src():


    @task()
    def ejecutar_prueba():
        main()

    ejecutar_prueba()

prueba_actualizacion_dags_src()
