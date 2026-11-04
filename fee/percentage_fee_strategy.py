__author__ = "Eric Tarrant"
__version__ = "1.0.0"

from decimal import Decimal
from fee.fee_strategy import FeeStrategy

class PercentageFeeStrategy(FeeStrategy):

    def __init__(
        self,
        percentage: Decimal
    ) -> None:

        if not 0 <= percentage <= 1:
            raise ValueError("percentage must be a value between 0 and 1 (inclusive)")

        self.__percentage = percentage

    @property
    def percentage(self) -> Decimal:

        return self.__percentage

    def get_fee(self, transcation_amount: Decimal) -> Decimal:

        return  round(transcation_amount * self.__percentage, 2) 