from airflow import Dataset
from airflow.decorators import dag, task
from pendulum import datetime
import os
import sys

#Path de carpeta
path_dag = os.path.dirname(os.path.dirname(__file__))
path_prueba = os.path.join(path_dag,"src","scrapingTrabajo")
sys.path.append(path_prueba)


#PRUEBA con SCRIPT DE EMAE
path_emae = os.path.join(path_prueba,"scrap_EMAE")
sys.path.append(path_emae)

#PRUEBA con SUPERMERCADO
path_supermercado = os.path.join(path_prueba,"scrap_Supermercados")
sys.path.append(path_supermercado)
print(sys.path)

from scrap_EMAE.main import main as emae_main
from scrap_Supermercados.main import main as super_main

# Definir el DAG
@dag(
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
)
def ejecutar_bloque_a():


    @task()
    def emae_prueba():
        emae_main()

    @task()
    def super_prueba():
        super_main()


    emae_prueba() >> super_prueba()

ejecutar_bloque_a()