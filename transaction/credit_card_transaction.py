from decimal import Decimal

from account.account_status import AccountStatus
from account.bank_account import BankAccount
from transaction.transaction import Transaction
from transaction.transaction_status import TransactionStatus


class CreditCardTransaction(Transaction):
    FEE_RATE = Decimal("0.02")

    def __init__(
        self,
        transaction_id: str,
        amount: Decimal,
        account: BankAccount,
        authorization_code: str
    ):
        if transaction_id.strip() == "":
            raise ValueError("transaction_id cannot be blank")

        if amount <= 0:
            raise ValueError("amount must be greater than zero")

        super().__init__(transaction_id, amount, account)
        self.__authorization_code = authorization_code

    @property
    def authorization_code(self) -> str:
        return self.__authorization_code

    @property
    def fees(self) -> Decimal:
        return self.amount * self.FEE_RATE

    def process(self) -> None:
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
        return (
            f"ID: {self.transaction_id}\n"
            f"STATUS: {self.status.name}\n"
            f"AMOUNT: ${self.amount:,.2f}\n"
            f"SOURCE ACCT: {self.account.account_id}\n"
            f"AUTH CODE: {self.authorization_code}"
        )