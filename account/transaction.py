__author__ = "Eric Tarrant"
__version__ = "1.0.0"

from account.transaction_status import TransactionStatus
from decimal import Decimal

class Transaction:
    def __init__(
    transaction_id: str,
    account: decimal.Decimal,
    status: TransactionStatus
    account: BankAccount):

    if transaction_id == "":
        raise ValueError("transaction_id cannot be blank.")
    if account <= 0:
        raise ValueError("account must be a value greater than zero.")
    self.__transaction_id = transaction_id
    self.__account = account
    self.__status = status
    
