__author__ = "Eric Tarrant"
__version__ = "1.0.0"
from account.transaction_status import TransactionStatus
from decimal import Decimal
from account.bank_account import BankAccount


class CreditCardTransaction:
    def __int__(
            self,
            transaction_id: str,
            amount: Decimal,
            account: BankAccount,
            authorization_code: str):