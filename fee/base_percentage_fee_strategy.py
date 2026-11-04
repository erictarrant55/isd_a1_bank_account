__author__ = "Eric Tarrant"
__version__ = "1.0.0"

from decimal import Decimal
from fee.fee_strategy import FeeStrategy


class BasePercentageFeeStrategy(FeeStrategy):

    def __init__(
        self,
        base_fee: Decimal,
        percentage: Decimal
    ) -> None:

        if base_fee < 0:
            raise ValueError("base_fee must be greater than or equal to zero")
        
        if not 0 <= percentage <= 1:
            raise ValueError("percentage must be a value between 0 and 1 (inclusive)")
        
        self.__percentage = percentage
        self.__base_fee = base_fee

    @property
    def percentage(self) -> Decimal:

        return self.__percentage

    @property
    
    def base_fee(self) -> Decimal:
    
        return self.__base_fee

    def base_percentage_fee_strategy(self, base_fee: Decimal, percentage: Decimal) -> Decimal:

        pass

    def get_fee(self, transaction_amount: Decimal) -> Decimal:
        percentage_fee = transaction_amount * self.__percentage

        if percentage_fee > self.__base_fee:
            return round(percentage_fee, 2)

        return round(self.__base_fee, 2)