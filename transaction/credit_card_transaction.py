from transaction.transaction_status import TransactionStatus
from decimal import Decimal
from account.bank_account import BankAccount

__author__ = "Eric Tarrant"
__version__ = "1.0.0"

class CreditCardTransaction:
    def __int__(
        self,
        transaction_id: str,
        amount: Decimal,
        account: BankAccount,
        authorization_code: str):

    if transaction_id == "":
        raise ValueError("transaction_id cannot be blank.")

    if account <= 0:
        raise ValueError("account must be a greater value than zero.")

    self.__transaction_id = transaction_id
    self.__amount = amount
    self.__account = account
    self.__authorization_code = authorization_code

    @property 
    def fees(self) -> Decimal:
        """
        Return the fees associated with the credit card transaction.

        Returns:
            decimal.Decimal: The fees associated with the credit card transaction.
        """

        return self.__fees

    def process() -> None:
        """
        Process the credit card transaction.

        This method would typically involve validating the transaction,
        checking for sufficient funds, and updating the account balance.
        """
        pass  

    def __str__(self) -> str:
        """
        Return a string representation of the credit card transaction.

        Returns:
            str: A string representation of the credit card transaction.
        """
        return f"CreditCardTransaction(transaction_id={self.__transaction_id}, amount={self.__amount}, account={self.__account}, authorization_code={self.__authorization_code})"