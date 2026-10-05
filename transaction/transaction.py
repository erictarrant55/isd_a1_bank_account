from abc import ABC, abstractmethod

from transaction.transaction_status import TransactionStatus  # adjust to your path


class Transaction(ABC):
    def __init__(
            self, 
            transaction_id, 
            amount, 
            account):
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
        return self.__transaction_id

    @property
    def amount(self):
        return self.__amount

    @property
    def account(self):
        return self.__account

    @property
    def status(self):
        return self._status

    @property
    @abstractmethod
    def fees(self):
        pass

    @abstractmethod
    def process(self):
        pass

    def __str__(self):
        return (
            f"ID: {self.transaction_id}\n"
            f"STATUS: {self.status.name}\n"
            f"AMOUNT: ${self.amount:,.2f}\n"
            f"SOURCE ACCT: {self.account.account_id}"
        )