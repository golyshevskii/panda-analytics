from scripts.objects.logger import logger
from scripts.objects.sender import MessageSender
from telegram import Bot


class TelegramMessageSender(MessageSender):
    def __init__(self, bot_token: str, chat_id: str):
        self.bot = Bot(bot_token)
        self.chat_id = chat_id

    def send_message(self, message: str):
        logger.info(f"Sending chat {self.chat_id} message...")

        self.bot.send_message(chat_id=self.chat_id, text=message)
        
        logger.info(f"Message has been sent successfully")
