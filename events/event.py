__author__ = "Eric Tarrant"
__version__ = "1.0.0"

from events.event_listener import EventListener

class Event(EventListener):
    def __init__(
        self,
        listeners: list[EventListener]
    ) -> None:

        self._listeners = listeners

    def event(self):
        
        pass

    def add_listener(self, listener: EventListener) -> None:

        
        return self._listeners + listener

    def remove_listener(self, listener: EventListener) -> None:

        return self._listeners - listener

    def notify(self, sender: object) -> None:
        if self.add_listener and self.remove_listener:
            for listener in self._listeners:
                listener.update(sender)
        pass