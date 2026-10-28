__author__ = "Eric Tarrant"
__version__ = "1.0.0"

from abc import ABC, abstractmethod

class EventListener(ABC):

    @abstractmethod
    def update(self, sender: object) -> None:

        pass