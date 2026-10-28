__author__ = "Eric Tarrant"
__version__ = "1.0.0"

from decimal import Decimal
from abc import ABC, abstractmethod


class FeeStrategy(ABC):

    @abstractmethod
    def get_fee(self, transaction_amount: Decimal) -> Decimal:

        pass
