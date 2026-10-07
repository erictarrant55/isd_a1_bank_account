from decimal import Decimal

from account.account_status import AccountStatus
from account.bank_account import BankAccount
from transaction.transaction import Transaction
from transaction.transaction_status import TransactionStatus


class CreditCardTransaction(Transaction):
    """
    Represents a credit card payment from a bank account.
 
    The CreditCardTransaction class stores information about a credit card
    payment, which includes the transaction_id, amount, account, authorization
    code and the status of the transaction. The payment is carried out
    when process() is called. The fee is charged to the account as well as
    to the amount.
 
    Attributes:
        FEE_RATE (Decimal): Percentage fee applied to the amount (2%).
        transaction_id (str): Unique identifier for the transaction.
        amount (Decimal): Amount of the payment.
        account (BankAccount): Account the amount and fees are withdrawn from.
        authorization_code (str): Code authorizing the payment.
        status (TransactionStatus): Current status of the transaction.
        fees (Decimal): Fee for the payment, calculated as amount * FEE_RATE.
 
    Raises:
        ValueError: If transaction_id is blank.
        ValueError: If amount is less than or equal to zero.
    """
    
    FEE_RATE = Decimal("0.02")

    def __init__(
        self,
        transaction_id: str,
        amount: Decimal,
        account: BankAccount,
        authorization_code: str
    ):
        """
        Creates a new credit card transaction.
 
        Args:
            transaction_id (str): Unique identifier for the transaction
            Must not be blank

            amount (Decimal): Amount of the payment must be greater than zero.

            account (BankAccount): The account the payment is charged to.
            
            authorization_code (str): Code authorizing the payment.
 
        Raises:
            ValueError: If transaction_id is blank.
            ValueError: If amount is less than or equal to zero.
        """
        if transaction_id.strip() == "":
            raise ValueError("transaction_id cannot be blank")

        if amount <= 0:
            raise ValueError("amount must be greater than zero")

        super().__init__(transaction_id, amount, account)
        self.__authorization_code = authorization_code

    @property
    def authorization_code(self) -> str:
        """
        Returns the authorization code of the payment.
 
        Returns:
            str: The code authorizing the payment.
        """
        return self.__authorization_code

    @property
    def fees(self) -> Decimal:
        """
        Calculates the fee charged to the account.
 
        The fee is the amount multiplied by FEE_RATE.
 
        Returns:
            Decimal: The fee charged for the payment.
        """
        return self.amount * self.FEE_RATE

    def process(self) -> None:
        """
        Attempts to execute the payment.
 
        The payment fails if the account is not active, if the account
        balance cannot cover the amount plus fees, or if the authorization
        code is blank. Otherwise, if the transaction is pending, the amount
        and fees are withdrawn from the account and the status is set to
        PROCESSED.
        """
        if (self.account.status != AccountStatus.ACTIVE
                or self.amount + self.fees > self.account.balance
                or self.authorization_code.strip() == ""):
            self._status = TransactionStatus.FAILED
            return

        if self.status == TransactionStatus.PENDING:
            self.account.withdraw(self.amount)
            self.account.withdraw(self.fees)
            self._status = TransactionStatus.PROCESSED

    def __str__(self) -> str:
        """
        Returns a string representation of the transaction.
 
        Returns:
            str: A string representation of the transaction.
        """
        return (
            f"ID: {self.transaction_id}\n"
            f"STATUS: {self.status.name}\n"
            f"AMOUNT: ${self.amount:,.2f}\n"
            f"SOURCE ACCT: {self.account.account_id}\n"
            f"AUTH CODE: {self.authorization_code}"
        )