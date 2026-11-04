__author__ = "Eric Tarrant"
__version__ = "1.0.0"

from events.event_listener import EventListener

 
 
class Event:
    """An object's event; notifies its listeners when raised."""
 
    def __init__(self):
        self.__listeners: list[EventListener] = []
 
    def add_listener(self, listener: EventListener) -> None:
        self.__listeners.append(listener)
 
    def remove_listener(self, listener: EventListener) -> None:
        if listener in self.__listeners:
            self.__listeners.remove(listener)
 
    def notify(self, sender: object) -> None:
        for listener in list(self.__listeners):
            listener.update(sender)