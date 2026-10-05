from enum import Enum

__author__ = "Eric Tarrant"
__version__ = "1.0.0"

class TransactionStatus(int, Enum):
    """
    Represents the status of a bank account transaction.
    
    TransactionStatus is an enumeration that is used to check the
    transaction status.
    
    
    Attributes:
            PENDING (int): Account is currently pending.
            PROCESSING (int): Account is processing.
            FAILED (int): Account has failed.
    """
    PENDING = 1
    PROCESSED = 2
    FAILED = 3