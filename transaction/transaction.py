from abc import ABC, abstractmethod

from transaction.transaction_status import TransactionStatus  # adjust to your path


class Transaction(ABC):
    """
    Represents a transaction that was made on a bank account.
 
    The Transaction class stores the information shared by all transactions, 
    which includes the transaction_id, amount, account and the status of the
    transaction. Subclasses must define how fees are calculated and how the 
    transaction is processed. 
     
    Attributes:
        transaction_id (str): Unique identifier for the transaction.
        amount (Decimal): Amount of the transaction.
        account (BankAccount): Account the transaction is made on.
        status (TransactionStatus): Current status of the transaction.
        fees (Decimal): Fee charged for the transaction. Defined by subclasses.
 
    Raises:
        ValueError: If transaction_id is blank.
        ValueError: If amount is less than or equal to zero.
    """
    def __init__(
            self, 
            transaction_id, 
            amount, 
            account):
        """
        Creates a new transaction.
 
        Args:
            transaction_id (str): Unique identifier for the transaction
            must not be blank.

            amount (Decimal): Amount of the transaction
            must be greater than zero.

            account (BankAccount): The account the transaction is made on.
 
        Raises:
            ValueError: If transaction_id is blank.
            ValueError: If amount is less than or equal to zero.
        """
        if transaction_id.strip() == "":
            raise ValueError("transaction_id cannot be blank")
        if amount <= 0:
            raise ValueError("amount must be greater than zero")

        self.__transaction_id = transaction_id
        self.__amount = amount
        self.__account = account
        self._status = TransactionStatus.PENDING
        
    @property
    def transaction_id(self):
        """
        Returns the transaction ID.
 
        Returns:
            str: The identifier that represents the transaction.
        """
        return self.__transaction_id

    @property
    def amount(self):
        """
        Returns the amount of the transaction.
 
        Returns:
            BankAccount: the amount of the transaction.
        """
        return self.__amount

    @property
    def account(self):
        """
        Returns the account the transaction is made on.
 
        Returns:
            BankAccount: The source account of the transaction.
        """
        return self.__account

    @property
    def status(self):
        """
        Returns the transaction status.
 
        Returns:
            TransactionStatus: The current status of the transaction.
        """    
        return self._status

    @property
    @abstractmethod
    def fees(self):
        """
        Calculates the fee charged for the transaction.
 
        Must be implemented by subclasses.
 
        Returns:
            Decimal: The fee charged for the transaction.
        """
        pass

    @abstractmethod
    def process(self):
        """
        Attempts to execute the transaction.
 
        Must be implemented by subclasses. The outcome is stored in the
        transaction's status.
        """
        pass

    def __str__(self):
        """
        Returns a string representation of the transaction.
 
        Returns:
            str: A string representation of the transaction.
        """
        return (
            f"ID: {self.transaction_id}\n"
            f"STATUS: {self.status.name}\n"
            f"AMOUNT: ${self.amount:,.2f}\n"
            f"SOURCE ACCT: {self.account.account_id}"
        )