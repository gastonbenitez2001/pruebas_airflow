from airflow import Dataset
from airflow.decorators import dag, task
from pendulum import datetime
import os
import sys

#Path de carpeta
path_dag = os.path.dirname(os.path.dirname(__file__))
path_prueba = os.path.join(path_dag,"src")

path_src = os.path.join(path_dag,"src","repositorio_para_airflow")

print(path_src)


#from repositorio_para_airflow.prueba_print import main
from scrapingTrabajo import scrap_EMAE as emae


from scrapingTrabajo import scrap_EMAE as emae

emae.main.main()

# Definir el DAG
@dag(
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
)
def print_hola_mundo():

    # Definir la tarea
    #@task
    #def main_prueba():
    #   main()

    @task()
    def emae_prueba():
        emae.main.main()

    emae_prueba()

print_hola_mundo()
