from airflow import Dataset
from airflow.decorators import dag, task
from pendulum import datetime
import requests
import os
import sys

#Path de carpeta
path_dag = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
path_src = os.path.join(path_dag,"src","repositorio_para_airflow")
path_prueba_print = os.path.join(path_src,"prueba_print")

sys.path.append(path_src)

from prueba_print import main


# Definir el DAG
@dag(
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
)
def print_hola_mundo():

    # Definir la tarea
    @task
    def main_prueba():
        main()

    main_prueba()

print_hola_mundo()
