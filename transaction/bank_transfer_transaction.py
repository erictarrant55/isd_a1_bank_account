from account.account_status import AccountStatus              # adjust paths
from transaction.transaction import Transaction
from transaction.transaction_status import TransactionStatus
from decimal import Decimal

class BankTransferTransaction(Transaction):
    BASE_FEE = Decimal("1.00")
    FEE_RATE = Decimal("0.007")
    def __init__(self, transaction_id, amount, account, target_account):
        super().__init__(transaction_id, amount, account)
        self.__target_account = target_account

    @property
    def target_account(self):
        return self.__target_account

    @property
    def fees(self):
        return max(self.BASE_FEE, self.amount * self.FEE_RATE)

    def process(self):
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
        return (
            f"ID: {self.transaction_id}\n"
            f"STATUS: {self.status.name}\n"
            f"AMOUNT: ${self.amount:,.2f}\n"
            f"SOURCE ACCT: {self.account.account_id} --> "
            f"TARGET ACCT: {self.target_account.account_id}"
        )