from abc import ABC, abstractmethod


class Sender(ABC):
    """Abstract class for sending messages"""

    @abstractmethod
    def send_message(self, message: str):
        pass
