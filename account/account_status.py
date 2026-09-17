from enum import Enum

class AccountStatus(int, Enum):
    """
    Represents the status of a bank account.

    AccountStatus is an enumeration that is used to identify
    the state of a bank account.

    Attributes:
        INACTIVE (int): Account is currently inactive.
        ACTIVE (int): Account is active.
        SUSPENDED (int): Account has been suspended.
        CLOSED (int): Account has been closed.
    """    
    INACTIVE = 0
    ACTIVE = 1
    SUSPENDED = 2
    CLOSED = 3
        