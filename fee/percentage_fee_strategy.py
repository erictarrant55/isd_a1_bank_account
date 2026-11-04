__author__ = "Eric Tarrant"
__version__ = "1.0.0"

from decimal import Decimal
from fee.fee_strategy import FeeStrategy

class PercentageFeeStrategy(FeeStrategy):
    """
    Represents a fee strategy that calculates fees using a percentage
    of the transaction amount.
    """
    def __init__(
        self,
        percentage: Decimal
    ) -> None:
        """
        Initializes a new PercentageFeeStrategy instance.

        Args:
            percentage (Decimal): The percentage is used to calculate the fee.

        Raises:
            ValueError: If percentage is not between 0 and 1 (inclusive).
        """

        if not 0 <= percentage <= 1:
            raise ValueError("percentage must be a value between 0 and 1 (inclusive)")

        self.__percentage = percentage

    @property
    def percentage(self) -> Decimal:
        """
        Gets the percentage that is used to calculate the transaction fee.

        Returns:
            Decimal: The percentage value.
        """
        return self.__percentage

    def get_fee(self, transaction_amount: Decimal) -> Decimal:
        """
        Calculates the transaction fee using a percentage.

        Args:
            transaction_amount (Decimal): The amount of the transaction.

        Returns:
            Decimal: The calculated transaction fee is rounded to two decimal places.
        """
        return  round(transaction_amount * self.__percentage, 2) 