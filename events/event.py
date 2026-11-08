__author__ = "Eric Tarrant"
__version__ = "1.0.0"

from events.event_listener import EventListener
 
 
class Event:
    """
    Represents an event that will notify the registered listeners when it 
    is raised.
    """
 
    def __init__(self):
        self.__listeners: list[EventListener] = []
 
    def add_listener(self, listener: EventListener) -> None:
        """
        Adds a listener to the event.

        Args:
            listener (EventListener): The listener to be added.
        """
        self.__listeners.append(listener)
 
    def remove_listener(self, listener: EventListener) -> None:
        """
        Removes a listener from the event if it has been registered.

        Args:
            listener (EventListener): The listener to be removed.
        """
        if listener in self.__listeners:
            self.__listeners.remove(listener)
 
    def notify(self, sender: object) -> None:
        """
        It notifies if all registered listeners that an event has occurred.

        Args:
            sender (object): The object that triggered the event.
        """
        for listener in list(self.__listeners):
            listener.update(sender)
        pass