import unittest
from events.event_listener import EventListener
from transaction.transaction import Transaction
from decimal import Decimal
from account.account_status import AccountStatus
from account.bank_account import BankAccount
from account.client import Client
from transaction.credit_card_transaction import CreditCardTransaction
from events.logging_listener import LoggingListener

__author__ = "Eric Tarrant"
__version__ = "1.0.0"


class TestInit(unittest.TestCase):
    """Defines tests for the __init__ method."""
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
 
        self.listener = LoggingListener()
 
    def test_sender_is_not_a_transaction(self) -> None:
        # Arrange
        sender = "not a transaction"
 
        # Act
        with self.assertRaises(TypeError) as context:
            self.listener.update(sender)
 
        # Assert
        expected = "sender must be a Transaction type"
        actual = str(context.exception)
        self.assertEqual(expected, actual)
    
    def test_initialize_new_instance(self) -> None:
        # Arrange
        listener = LoggingListener()

        # Act & Assert
        self.assertIsInstance(listener, LoggingListener)
        self.assertIsInstance(listener, EventListener)