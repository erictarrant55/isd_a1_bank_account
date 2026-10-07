from account.account_status import AccountStatus              # adjust paths
from transaction.transaction import Transaction
from transaction.transaction_status import TransactionStatus
from decimal import Decimal

class BankTransferTransaction(Transaction):
    """
    Represents a transfer of funds between two accounts.
 
    The BankTransferTransaction class stores information about a transfer,
    which includes the transaction_id, amount, source account, target account
    and the status of the transaction. The transfer is carried out when
    process() is called. The fee is paid by the source account, and the
    target account receives the full amount of money.
 
    Attributes:
        BASE_FEE (Decimal): Minimum fee charged on any transfer (1.00).
        FEE_RATE (Decimal): Percentage fee applied to the amount (0.7%).
        transaction_id (str): Unique identifier for the transaction.
        amount (Decimal): Amount to be transferred.
        account (Account): Source account the funds are withdrawn from.
        target_account (Account): Destination account the funds are deposited into.
        status (TransactionStatus): Current status of the transaction.
        fees (Decimal): Fee for the transfer, the greater of BASE_FEE and
            amount * FEE_RATE.
 
    Raises:
        ValueError: If transaction_id is blank.
        ValueError: If amount is less than or equal to zero.
    """    
    BASE_FEE = Decimal("1.00")
    FEE_RATE = Decimal("0.007")
    def __init__(self, transaction_id, amount, account, target_account):
        """
        Creates a new bank transfer transaction.
 
        Args:
            transaction_id (str): Unique identifier for the transaction.
            amount (Decimal): Amount to transfer, must be greater than zero.
            account (Account): The source account.
            target_account (Account): The destination account.
 
        Raises:
            ValueError: If transaction_id is blank.
            ValueError: If amount is less than or equal to zero.
        """
 
        if transaction_id.strip() == "":
            raise ValueError("transaction_id cannot be blank")

        if amount <= 0:
            raise ValueError("amount must be greater than zero")
        
        super().__init__(transaction_id, amount, account)
        self.__target_account = target_account

    @property
    def target_account(self):
        """
        Returns the account of the transfer.
 
        Returns:
            Account: The target account.
        """  
        
        return self.__target_account

    @property
    def fees(self):
        """
        Calculates the fee charged to the source account.
 
        The fee is the greater of BASE_FEE and amount * FEE_RATE.
 
        Returns:
            Decimal: The fee for this transfer.
        """
        
        return max(self.BASE_FEE, self.amount * self.FEE_RATE)

    def process(self):
        """
        Attempts to complete the transfer.
 
        The transfer fails if either of the accounts are is not active, 
        or if the source account balance cannot cover the amount as well as the 
        fees. Otherwise, if the transaction is pending, the amount and fees are 
        withdrawn from the source account, the amount is deposited into the 
        target account, and the status is set to PROCESSED.
        """
        if (self.account.status != AccountStatus.ACTIVE
                or self.target_account.status != AccountStatus.ACTIVE):
            self._status = TransactionStatus.FAILED
            return

        if self.amount + self.fees > self.account.balance:
            self._status = TransactionStatus.FAILED
            return

        if self.status == TransactionStatus.PENDING:
            self.account.withdraw(self.amount)
            self.account.withdraw(self.fees)
            self.target_account.deposit(self.amount)
            self._status = TransactionStatus.PROCESSED

    def __str__(self):
        """
        Returns a readable summary of the transaction.
 
        Returns:
            str: A readable summary of the transaction.
        """
        return (
            f"ID: {self.transaction_id}\n"
            f"STATUS: {self.status.name}\n"
            f"AMOUNT: ${self.amount:,.2f}\n"
            f"SOURCE ACCT: {self.account.account_id} --> "
            f"TARGET ACCT: {self.target_account.account_id}"
        )