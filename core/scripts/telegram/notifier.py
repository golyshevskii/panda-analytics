from config import PATH, TG_PABOT_TOKEN
from scripts.objects.configurator import Configurator
from scripts.objects.formatter import Formatter
from scripts.objects.logger import logger
from telegram import ParseMode

from .sender import TelegramSender


def notify_by_photo(config_path: str):
    """
    Notifies about metrics in the Telegram channel

    Params:
        config_path: Path to the yaml config file. See configs folder
    """
    logger.info("BEGIN")
    # Get config
    config = Configurator(config_path=config_path).get()

    # Format message
    formatter = Formatter(template_path=config["caption"])
    caption = formatter.fmessage(data={"dashboard": config["dashboard"]})

    # Get photo
    with open(f"{PATH}{config['photo']}", "rb") as file:
        photo = file.read()

    # Send notifications
    sender = TelegramSender(bot_token=TG_PABOT_TOKEN)
    for channel in config["notification"]["channels"]:
        sender.send_photo(
            chat_id=channel, photo=photo, parse_mode=ParseMode.HTML, caption=caption
        )

    logger.info("END")
