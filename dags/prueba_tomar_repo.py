
import sys
import os
from airflow.decorators import dag, task
from airflow.utils.trigger_rule import TriggerRule
from pendulum import datetime




direccion = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
direccion_repo = os.path.join(direccion,"repositorio")
direccion_scrapping = os.path.join(direccion_repo,"scrapingTrabajo")

#Prueba de scrip
direccion_script_emae = os.path.join(direccion_scrapping,"scrap_EMAE")

#direccion main
sys.path.append(direccion_scrapping)
#sys.path.append(direccion_scrapping)

from scrap_EMAE import main as emae
from DNRPA import main as dnrpa

# Definir el DAG
@dag(
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
)
def scrap_emae_dnrpa_dag():
    # Definir la primera tarea
    @task(trigger_rule=TriggerRule.ALL_DONE)
    def run_emae():
        emae.main()

    # Definir la segunda tarea
    @task(trigger_rule=TriggerRule.ALL_DONE)
    def run_dnrpa():
        dnrpa.main()

    # Definir la secuencia de tareas
    run_emae() >> run_dnrpa()

# Instanciar el DAG
scrap_emae_dnrpa_dag()