from enum import Enum

class AccountStatus(int, Enum):
    INACTIVE = 0
    ACTIVE = 1
    SUSPENDED = 2
    CLOSED = 3
        