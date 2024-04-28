from typing import Union

from scripts.objects.logger import logger
from scripts.objects.sender import Sender
from telegram import Bot, ParseMode


class TelegramSender(Sender):
    """
    Class for sending messages to the Telegram channel

    Attributes:
        bot: Telegram bot object
        chat_id: Telegram chat id where messages will be sent
    """

    def __init__(self, bot_token: str):
        self.bot = Bot(bot_token)

    def send_message(
        self,
        chat_id: Union[str, int],
        message: str,
        parse_mode: str = ParseMode.MARKDOWN,
        **kwargs,
    ):
        """
        Sends text message to the Telegram channel

        Params:
            message: Text message
            parse_mode: Markdown | MarkdownV2 or HTML
        """
        logger.info(f"Sending chat {chat_id} message...")

        self.bot.send_message(
            chat_id=chat_id, text=message, parse_mode=parse_mode, **kwargs
        )

        logger.info("Message has been sent successfully")

    def send_photo(
        self,
        chat_id: Union[str, int],
        photo: Union[str, bytes],
        parse_mode: str = ParseMode.MARKDOWN,
        **kwargs,
    ):
        """
        Sends photo to the Telegram channel

        Params:
            photo: Photo to send.
            Pass a file_id as String to send a file that exists on the Telegram servers (recommended).
            Pass an HTTP URL as a String for Telegram to get a file from the Internet.
            To upload a file, you can either pass a file object (e.g. open("filename", "rb"))
            parse_mode: Markdown | MarkdownV2 or HTML
        """
        logger.info(f"Sending chat {chat_id} photo...")

        self.bot.send_photo(
            chat_id=chat_id, photo=photo, parse_mode=parse_mode, **kwargs
        )

        logger.info("Photo has been sent successfully")
