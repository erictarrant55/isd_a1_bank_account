__author__ = "Eric Tarrant"
__version__ = "1.0.0"

from account.transaction_status import TransactionStatus
from decimal import Decimal
from account.bank_account import BankAccount

class BankTransferTransaction:
    def __init__(
        self,
        transaction_id: str,
        amount: Decimal,
        account: BankAccount,
        target_account: BankAccount):

        if transaction_id == "":
            raise ValueError("transaction_id cannot be blank.")

        if account <= 0:
            raise ValueError("account must be a value greater than zero.")

        self.__transaction_id = transaction_id
        self.__amount = amount
        self.__account = account
        self.__target_account = target_account

    # @property
    # def fees(self) -> Decimal:
    #     """
    #     Return the fees associated with the bank transfer transaction.

    #     Returns:
    #         decimal.Decimal: The fees associated with the bank transfer transaction.
    #     """
    #     return self.__fees

    # def process() -> None:

    def __str__(self) -> str:
        """
        Return a string representation of the bank transfer transaction.

        Returns:
            str: A string representation of the bank transfer transaction.
        """
        return f"BankTransferTransaction(transaction_id={self.__transaction_id}
        , amount={self.__amount}, account={self.__account}, target_account={self.__target_account})"

        