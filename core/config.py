import os

# SYSTEM
PATH = "/opt/airflow/dags/"

# PADWH
PADWH_CONN = os.environ.get("AIRFLOW_VAR_PADWH_CONN")

# TELEGRAM
TG_PABOT_TOKEN = os.environ.get("AIRFLOW_VAR_TG_PABOT_TOKEN")
TG_PAALERT_CHAT_ID = int(os.environ.get("AIRFLOW_VAR_TG_PAALERT_CHAT_ID"))
