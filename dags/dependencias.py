# Import all packages needed at the top level of the DAG
from airflow.decorators import dag, task
from pendulum import datetime
from airflow.utils.trigger_rule import TriggerRule

# Define the DAG function with a set of parameters
@dag(
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
)
def example_dag_with_error_handling():
    # Define the first task which will produce an error
    @task
    def task_that_fails():
        print("This task will fail.")
        raise ValueError("Intentional Error")

    # Define the second task which will run regardless of the first task's result
    @task(trigger_rule=TriggerRule.ALL_DONE)
    def task_that_always_runs():
        print("This task runs regardless of the previous task's result.")

    # Define dependencies and call task functions
    t1 = task_that_fails()
    t2 = task_that_always_runs()

    t1 >> t2

# Call the DAG function to instantiate the DAG
example_dag_with_error_handling()
