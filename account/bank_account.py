from account.account_status import AccountStatus

class BankAccount:
    def __init__(
        self,
        account_id,
        balance,
        owner,
        status=AccountStatus.ACTIVE):
        """Represents a bank account of a client."""
        
        if account_id <= 0:
            raise ValueError("account_id must be a value greater than zero.")

        self.__account_id = account_id
        self.__balance = balance
        self.__owner = owner
        self.__status = status

    @property
    def account_id(self) -> int:
        return self.__account_id

    @property
    def balance(self) -> float:
        return self.__balance

    @property
    def owner(self) -> str:
        return self.__owner

    @property
    def status(self) -> int:
        return self.__status

    def update_balance(self, amount: float) -> None:
        self.__balance = amount

    def deposit(self, amount: float) -> None:
        if amount < 0:
            raise ValueError("amount must be a value greater than or equal to zero.")
        self.__balance += amount

    def withdraw(self, amount):

        if amount < 0:
            raise ValueError(
                "amount must be a value greater than or equal to zero."
            )

        if amount > self.__balance:
            raise ValueError(
                "amount cannot exceed the account balance."
            )

        self.__balance -= amount
        
    def __str__(self) -> str:
            return (f"Account ID: {self.__account_id}\n"
                    f"Balance: {self.__balance}\n"
                    f"Owner: {self.__owner}\n"
                    f"Status: {self.__status}")
    
