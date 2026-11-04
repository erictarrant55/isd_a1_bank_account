import unittest
from contextlib import redirect_stdout
from decimal import Decimal
 
from account.account_status import AccountStatus
from account.bank_account import BankAccount
from account.client import Client
from events.event import Event
from events.logging_listener import LoggingListener
from transaction.credit_card_transaction import CreditCardTransaction
from events.event_listener import EventListener
__author__ = "Eric Tarrant"
__version__ = "1.0.0"

class TestNotifyListener(EventListener):
    """Counts how many times it was notified."""

    def __init__(self) -> None:
        self.count = 0

    def update(self, sender: object) -> None:
        self.count += 1

class TestInit(unittest.TestCase):
    def test_inilialize_new_istance(self) -> None:

        # Arrange
        # Act
        event = Event()
 
        # Assert
        self.assertEqual([], event._Event__listeners)

class TestAddListener(unittest.TestCase):
    """Defines tests for the add_listener method."""
 
    def test_listener_is_added(self) -> None:
        # Arrange
        event = Event()
        listener = LoggingListener()
 
        # Act
        event.add_listener(listener)
 
        # Assert
        self.assertEqual([listener], event._Event__listeners)

class TestRemoveListener(unittest.TestCase):
    """Defines tests for the remove_listener method."""
 
    def test_listener_is_not_a_listener(self) -> None:
        # Arrange
        event = Event()
        listener = LoggingListener()
 
        # Act
        event.remove_listener(listener)
 
        # Assert
        self.assertEqual([], event._Event__listeners)     
    def test_listener_is_removed(self) -> None:
        # Arrange
        event = Event()
        listener = LoggingListener()
        event.add_listener(listener)
 
        # Act
        event.remove_listener(listener)
 
        # Assert
        self.assertEqual([], event._Event__listeners) 

class TestNotify(unittest.TestCase):
    """Defines tests for the notify method."""
 
    def setUp(self) -> None:
        self.client = Client(
            1,
            "Eric Tarrant",
            "etarrant@rrc.ca"
        )
 
        self.account = BankAccount(
            123456,
            Decimal("5000.00"),
            self.client,
            AccountStatus.ACTIVE
        )
 
        self.transaction = CreditCardTransaction(
            "123",
            Decimal("100.00"),
            self.account,
            "AUTH123"
        )
 
        self.event = Event()
 
    def test_listener_is_notified(self) -> None:
        # Arrange
        listener = TestNotifyListener()
        self.event.add_listener(listener)

        # Act
        self.event.notify(object())

        # Assert
        self.assertEqual(1, listener.count)      
    
    def test_listener_is_not_notified(self) -> None:
        # Arrange
        listener = TestNotifyListener()
        self.event.remove_listener(listener)
    
        # Act
        self.event.notify(object())
    
        # Assert
        self.assertEqual(0, listener.count)   