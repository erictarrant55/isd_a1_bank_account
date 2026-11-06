__author__ = "Eric Tarrant"
__version__ = "1.0.0"

from abc import ABC, abstractmethod

class EventListener(ABC):
    """
    Represents an abstract listener that receives event notifications.
    """
    @abstractmethod
    def update(self, sender: object) -> None:
        """
        Updates the listener when an event occurs.

        Args:
            sender (object): The object that triggered the event.
        """
        pass