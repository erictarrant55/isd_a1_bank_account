__author__ = "Eric Tarrant"
__version__ = "1.0.0"

from decimal import Decimal

from account.account_status import AccountStatus
from account.bank_account import BankAccount
from acccount.transaction import Transaction
from account.transaction_status import TransactionStatus

class BankTransferTransaction(Transaction):
    """Represents a bank transfer transaction.
    
    transaction_id (str): The unique identifier for the transaction.
    amount (Decimal): The amount of money to be transferred.
    account (BankAccount): The source bank account for the transfer.
    target_account (BankAccount): The target bank account for the transfer.
    """
    
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

        super().__init__(transaction_id, amount, account)
        self.__target_account = target_account
    
    @property
    def fees(self) -> Decimal:
        """
        Return the fees associated with the bank transfer transaction.

        Returns:
            decimal.Decimal: The fees associated with the bank transfer transaction.
        """
        return max(1.00, self.__amount * 0.007)

    def process(self) -> None:
        if self.account.status != AccountStatus.ACTIVE:
            self._set_status(TransactionStatus.FAILED)
            return

        if self.target_account.status != AccountStatus.ACTIVE:
            self._set_status(TransactionStatus.FAILED)
            return

        if self.amount + self.fees > self.account.balance:
            self._set_status(TransactionStatus.FAILED)
            return

        if self.status != TransactionStatus.PENDING:
            return

        self.account.withdraw(self.amount)
        self.account.withdraw(self.fees)
        self.target_account.deposit(self.amount)

        self._set_status(TransactionStatus.PROCESSED)

    def __str__(self) -> str:
        """
        Return a string representation of the bank transfer transaction.

        Returns:
            str: A string representation of the bank transfer transaction.
        """
        return (
            f"ID: {self.transaction_id}\n"
            f"STATUS: {self.status.name}\n"
            f"AMOUNT: ${self.amount:,.2f}\n"
            f"SOURCE ACCT: {self.account.account_id} "
            f"TARGET ACCT: {self.target_account.account_id}"
        )