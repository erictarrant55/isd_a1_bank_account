__author__ = "Eric Tarrant"
__version__ = "1.0.0"

import unittest
from fee.percentage_fee_strategy import PercentageFeeStrategy
from account.client import Client
from account.bank_account import BankAccount
from fee.fee_strategy import FeeStrategy

class TestInit(unittest.TestCase):
    """Defines tests for the __init__ method."""

    def setUp(self) -> None:
        self.client = Client(
            1,
            "Eric Tarrant",
            "etarrant@rrc.ca"
        )
