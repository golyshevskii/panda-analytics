from typing import Any, Dict

from config import TG_PAALERT_CHAT_ID, TG_PABOT_TOKEN
from scripts.alerts.utils import build_task_fail_message
from scripts.objects.logger import logger
from scripts.telegram.sender import TelegramSender


def task_fail_alert(context: Dict[str, Any]) -> None:
    """
    Sends a message if Airflow task fails

    Params:
        context: Airflow DAG context
    """
    logger.info("Preparing to send a task fail alert...")
    message = build_task_fail_message(**context)

    sender = TelegramSender(bot_token=TG_PABOT_TOKEN)
    sender.send_message(chat_id=TG_PAALERT_CHAT_ID, message=message)
