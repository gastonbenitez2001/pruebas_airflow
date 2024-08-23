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

#PRUEBA con SCRIPT DE SUPERMERCADO
path_supermercado = os.path.join(path_prueba,"scrap_Supermercados")
sys.path.append(path_supermercado)
from scrap_Supermercados.main import main as main_supermercado


# Definir el DAG
@dag(
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
)
def ejecutar_bloque_a():


    @task()
    def emae_prueba():
        main_emae()

    @task()
    def supermercados():
        main_supermercado()


    emae_prueba() >> supermercados()

ejecutar_bloque_a()
