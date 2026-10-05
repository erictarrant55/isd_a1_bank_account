from account.transaction_status import TransactionStatus
from decimal import Decimal
from abc import abstractmethod, ABC

__author__ = "Eric Tarrant"
__version__ = "1.0.0"

class Transaction:
    def __init__(
        self,
        transaction_id: str,
        amount: Decimal,
        status: TransactionStatus,
        account: BankAccount):

    if transaction_id == "":
        raise ValueError("transaction_id cannot be blank.")
    if account <= 0:
        raise ValueError("account must be a value greater than zero.")
    self.__transaction_id = transaction_id
    self.__account = account
    self.__status = status


    @property
    def transaction_id(self) -> str:
        """
        Return the transaction ID.

        Returns:
            str: The identifier that represents the transaction.
        """
        return self.__transaction_id

    @property
    def acount(self) -> Decimal:
        """
        Return the account.

        Returns:
            decimal.Decimal: The account associated with the transaction.
        """
        return self.__account

    @property
    def status(self) -> TransactionStatus:
        """
        Return the transaction status.

        Returns:
            TransactionStatus: The status of the transaction.
        """
        return self.__status

    @property
    def account(self) -> BankAccount:
        """
        Return the account associated with the transaction.

        Returns:
            BankAccount: The bank account associated with the transaction.
        """
        return self.__account

    @property
    @abstractmethod
    def fees(self) -> Decimal:
        """
        Return the transaction fees.

        Returns:
            decimal.Decimal: The fees associated with the transaction.
        """
        return self.__fees

    @abstractmethod
    def process() -> None:    
        """
        Process the transaction.

        This method should be implemented in subclasses to define
        specific transaction processing logic.
        """
        return self.__process

    def __str__(self) -> str:
        """
        Return a string representation of the transaction.

        Returns:
            str: A string representation of the transaction.
        """
        return (
            f"ID: {self.transaction_id}\n"
            f"STATUS: {self.status.name}\n"
            f"AMOUNT: ${self.amount:,.2f}\n"
            f"SOURCE ACCT: {self.account.account_id}"
        )