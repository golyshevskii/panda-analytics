from scripts.objects.logger import logger
from scripts.tools.psql.client import PSQLClient
from ..tgsender import TelegramMessageSender
import pandas as pd

from config import TG_PABOT_TOKEN, PADWH_CONN


def manage(**kwargs):
    """Manages"""
    logger.info("BEGIN")

    # Import metrics
    psql = PSQLClient(conn_str=PADWH_CONN)
    data: pd.DataFrame = psql.select(query=kwargs["sql"])

    message = ""
    
    # Send message
    sender = TelegramMessageSender(bot_token=TG_PABOT_TOKEN, chat_id=kwargs["chat_id"])
    sender.send_message(message=message)

    logger.info("END")
