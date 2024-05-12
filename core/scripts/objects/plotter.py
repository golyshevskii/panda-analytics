from abc import ABC, abstractmethod


class Plotter(ABC):
    """Abstract Class for plotting metrics"""

    @abstractmethod
    def plot(self, **kwargs):
        pass
