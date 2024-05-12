Quick Start
---

### Настройка DAG

Для настройки DAG используйте Python-скрипты. В каждом Python-скрипте определите экземпляр класса `DAG` с нужными параметрами и задачи, которые должны выполняться в этом DAG.

Пример Python-скрипта для определения DAG:

```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


with DAG(
    dag_id='my_dag',
    schedule_interval='@daily',
    start_date=datetime(2023, 1, 1)
) as dag:
    task1 = PythonOperator(
        task_id='task1',
        python_callable=my_python_function
    )
```

> Задачи в DAG будут помещены в соответствующие очереди, где воркеры Celery будут обрабатывать их в соответствии с настройками запуска
