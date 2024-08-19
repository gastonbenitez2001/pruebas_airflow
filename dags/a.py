from airflow import Dataset
from airflow.decorators import dag, task
from pendulum import datetime
import os
import sys

#Path de carpeta
path_dag = os.path.dirname(os.path.dirname(__file__))
path_prueba = os.path.join(path_dag,"src","scrapingTrabajo")
sys.path.append(path_prueba)

#path_src = os.path.join(path_dag,"src","repositorio_para_airflow")
#Agregamos ruta del proyecto y del SRC para acceder a multiples archivos
#path_folder_github = os.path.join(path_dag,"src","scrapingTrabajo")


#sys.path.append(path_src)
#sys.path.append(path_folder_github)


#from prueba_print import main


#PRUEBA con SCRIPT DE EMAE
path_emae = os.path.join(path_prueba,"scrap_EMAE")
sys.path.append(path_emae)

from scrap_EMAE.main import main as main_emae

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
        main_emae()


    emae_prueba()

print_hola_mundo()
