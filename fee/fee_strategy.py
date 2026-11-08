__author__ = "Eric Tarrant"
__version__ = "1.0.0"

from decimal import Decimal
from abc import ABC, abstractmethod


class FeeStrategy(ABC):
    """
    Represents a strategy for calculating fees based on a transaction amount.
    """
    @abstractmethod
    def get_fee(self, transaction_amount: Decimal) -> Decimal:
        """
        Calculates a fee that is a given transaction amount.

        Args:
            transaction_amount (Decimal): The amount of the transaction.

        Returns:
            Decimal: The calculated transaction fee.
        """
        pass
