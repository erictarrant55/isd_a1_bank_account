from account.account_status import AccountStatus


class BankAccount:
    def __init__(
        self,
        account_id,
        balance,
        owner,
        status=AccountStatus.ACTIVE):
        """Represents a bank account of a client."""
        
        self.account_id = account_id
        self.balance = balance
        self.owner = owner
        self.status = status

