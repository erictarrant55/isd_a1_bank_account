__author__ = "Eric Tarrant"
__version__ = "1.0.0"

from decimal import Decimal
from fee.fee_strategy import FeeStrategy


class BasePercentageStrategy(FeeStrategy):

    def __init__(
        self,
        base_fee: Decimal,
        percentage: Decimal
    ) -> None:

        if base_fee >= 0:
            raise ValueError("base_fee must be greater than or equal to zero")
        
        if not 0 <= percentage <= 1:
            raise ValueError("percentage must be a value between 0 and 1 (inclusive)")
        
        self._percentage = percentage
        self._base_fee = base_fee

    @property
    def percentage(self) -> Decimal:

        return self._percentage

    @property
    
    def base_fee(self) -> Decimal:
    
        return self._base_fee

    def base_percentage_fee_strategy(self, base_fee: Decimal, percentage: Decimal) -> Decimal:

        pass

    def get_fee(self, transaction_amount: Decimal) -> Decimal:

        return self._base_fee + (transaction_amount * self._percentage)