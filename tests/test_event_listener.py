import unittest
 
from events.event_listener import EventListener
__author__ = "Eric Tarrant"
__version__ = "1.0.0"
 
 
class IncompleteListener(EventListener):
    """Subclass that does not implement update."""
    pass
 
 
class CompleteListener(EventListener):
    """Subclass that implements update."""
 
    def update(self, sender: object) -> None:
        pass
 
 
class TestInit(unittest.TestCase):
    """Defines tests for the EventListener interface."""
 
    def test_interface_cannot_be_instantiated(self) -> None:
        # Arrange
        # Act
        with self.assertRaises(TypeError):
            EventListener()
 
        # Assert
 
    def test_subclass_without_update_cannot_be_instantiated(self) -> None:
        # Arrange
        # Act
        with self.assertRaises(TypeError):
            IncompleteListener()
 
        # Assert
 
    def test_subclass_with_update_can_be_instantiated(self) -> None:
        # Arrange
        # Act
        listener = CompleteListener()
 
        # Assert
        self.assertIsInstance(listener, EventListener)