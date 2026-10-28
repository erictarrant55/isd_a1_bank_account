__author__ = "Eric Tarrant"
__version__ = "1.0.0"

from abc import ABC, abstractmethod

class EventListener(ABC):

    def update(self,sender: object) -> None:

        pass