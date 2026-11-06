__author__ = "Eric Tarrant"
__version__ = "1.0.0"

from decimal import Decimal
from fee.fee_strategy import FeeStrategy


class BasePercentageFeeStrategy(FeeStrategy):
    """
    Represents a fee strategy that calculates fees based on a base fee and a 
    percentage of the transaction amount, it is subject to the base limit fee.
    """
    def __init__(
        self,
        base_fee: Decimal,
        percentage: Decimal
    ) -> None:
        """
        Initializes a new BasePercentageFeeStrategy instance.

        Args:
            base_fee (Decimal): The maximum fee that can be charged.
            percentage (Decimal): The percentage to calculate the fee.

        Raises:
            ValueError: If base_fee is less than zero.
            ValueError: If percentage is not between 0 and 1 (inclusive).
        """

        if base_fee < 0:
            raise ValueError("base_fee must be greater than or equal to zero")
        
        if not 0 <= percentage <= 1:
            raise ValueError("percentage must be a value between 0 and 1 (inclusive)")
        
        self.__percentage = percentage
        self.__base_fee = base_fee

    @property
    def percentage(self) -> Decimal:
        """
        Gets the percentage used to calculate the transaction fee.

        Returns:
            Decimal: The percentage value.
        """
        return self.__percentage

    @property
    
    def base_fee(self) -> Decimal:
        """
        Gets the maximum fee that can be charged.

        Returns:
            Decimal: The base fee amount.
        """
        return self.__base_fee

    def base_percentage_fee_strategy(self, base_fee: Decimal, percentage: Decimal) -> Decimal:
        """
        Calculates the fee by using the base fee and percentage.

        Args:
            base_fee (Decimal): The maximum fee amount.
            percentage (Decimal): The percentage that calculates the fee.

        Returns:
            Decimal: The calculated fee amount.
        """
        return round(percentage * base_fee, 2)

    def get_fee(self, transaction_amount: Decimal) -> Decimal:
        percentage_fee = transaction_amount * self.__percentage
        """
        Calculates the transaction fee based on a percentage
        as well as the base fee limit.

        Args:
            transaction_amount (Decimal): The transaction amount.

        Returns:
            Decimal: The calculated transaction fee is rounded to two decimal places.
        """
        if percentage_fee > self.__base_fee:
            return round(self.__base_fee, 2)

        return round(percentage_fee, 2)