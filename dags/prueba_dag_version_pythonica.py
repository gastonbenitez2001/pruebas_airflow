# Import all packages needed at the top level of the DAG
from airflow.decorators import dag, task
from airflow.models.baseoperator import chain
from pendulum import datetime


#DEFINICION DEL DAG (En el se define los datos basicos que usara la automatizacion)
@dag(
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
)

#En esta funcion creamos las tareas que el dag ejecutara, podemos crear dependencias entre tareas.
def taskflow_dag():

    # Define tasks within the DAG context
    @task
    def my_task_1():
        print("************************")
        print("Esta es la primera tarea")
        print("************************")

    @task
    def my_task_2():
        print(2)

    # Define dependencies and call task functions
    my_task_1()




# Call the DAG function
taskflow_dag()