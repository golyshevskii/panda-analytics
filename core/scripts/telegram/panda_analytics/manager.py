import pandas as pd
from config import PADWH_CONN, TG_PABOT_TOKEN
from scripts.objects.logger import logger
from scripts.tools.psql.client import PSQLClient

from ..tgsender import TelegramMessageSender


def manage(**kwargs):
    """Manages"""
    logger.info("BEGIN")

    # Import metrics
    psql = PSQLClient(conn_str=PADWH_CONN)
    _: pd.DataFrame = psql.select(query=kwargs["sql"])

    message = ""

    # Send message
    sender = TelegramMessageSender(bot_token=TG_PABOT_TOKEN, chat_id=kwargs["chat_id"])
    sender.send_message(message=message)

    logger.info("END")
