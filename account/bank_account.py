from account.account_status import AccountStatus


class BankAccount:
    def __init__(
        self,
        account_id,
        balance,
        owner,
        status=AccountStatus.ACTIVE):
        """Represents a bank account of a client."""
        
        if len(account_id.strip()) <= 0:
            raise ValueError("account_id must be a value greater than 0.")

        self.__account_id = account_id
        self.__balance = balance
        self.__owner = owner
        self.__status = status

    @property
    def account_id(self) -> int:
        return self.account_id

    @property
    def balance(self) -> balance:
        return self.balance

    @property
    def owner(self) -> str:
        return self.owner

    @property
    def status(self) -> int:
        return self.status

    def update_balance(self, balance):
        self.balance = balance

    def deposit(self, balance):
        if balance >= 0:
            raise ValueError("Amount must be a value greater than"
        "or equal to zero.")
        self.balance += balance

    def withdraw(self, balance):
        if balance < 0:
            raise ValueError("Amount must be a value greater than ir equal" \
            "to zero.")

        self.balance -+ balance
    def __str__(self) -> str:
            return (f"Account ID: {self.__account_id()}\n"
                    f"Balance: {self.__balance()}\n"
                    f"Owner: {self.__owner()}\n"
                    f"Status: {self.__status}")
