from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from scripts.alerts.sender import task_fail_alert
from scripts.telegram.notifier import notify_by_photo
from scripts.tools.mplot.plot import plot_daily_metrics

with DAG(
    dag_id="notifier_panda_analytics",
    description="Notifies about Panda Analytics metrics",
    tags=["panda-analytics", "basic", "notifier"],
    schedule=None,
    start_date=datetime(2024, 5, 1),
    dagrun_timeout=timedelta(minutes=60),
    catchup=False,
    max_active_runs=1,
    default_args={
        "owner": "PA",
        "retries": 1,
        "retry_delay": timedelta(minutes=1),
        "on_failure_callback": task_fail_alert,
    },
) as dag:
    CONFIG_PATH = "configs/basic/panda-analytics.yaml"

    start = EmptyOperator(task_id="start")

    plot__daily_metrics = PythonOperator(
        task_id="plot__daily_metrics",
        python_callable=plot_daily_metrics,
        op_kwargs={"config_path": CONFIG_PATH},
    )

    notify__by_photo = PythonOperator(
        task_id="notify__by_photo",
        python_callable=notify_by_photo,
        op_kwargs={"config_path": CONFIG_PATH},
    )

    end = EmptyOperator(task_id="end")

    start >> plot__daily_metrics >> notify__by_photo >> end
