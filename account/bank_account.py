from account.account_status import AccountStatus

class BankAccount:
    """
    Represents a bank account to a client.

    The BankAccount class stores information about a bank account,
    which includes the account_id, balance, owner and the status of the
    account.

    Attributes:
        account_id (int): Unique identifier for the account.
        balance (float): the Balance of the account.
        owner (str): Name of the account owner.
        status (AccountStatus): Current status of the account.

    Raises:
        ValueError: If account_id is less than or equal to zero.
    """
    def __init__(
        self,
        account_id,
        balance,
        owner,
        status=AccountStatus.ACTIVE):
        """Represents a new bank account of a client.
        
        Args:
            account_id (int): Unique identifier for the account.
                Must be greater than zero.
            balance (float): Initial balance of the account.
            owner (str): Name of the account owner.
            status (AccountStatus, optional): Initial account status.
                Defaults to AccountStatus.ACTIVE.

        Raises:
            ValueError: If account_id is less than or equal to zero.
        """
        
        if account_id <= 0:
            raise ValueError("account_id must be a value greater than zero.")

        self.__account_id = account_id
        self.__balance = balance
        self.__owner = owner
        self.__status = status

    @property
    def account_id(self) -> int:
        """
        Return the account ID.

        Returns:
            int: The identifier that represents the bank account."
        """
        return self.__account_id

    @property
    def balance(self) -> float:
        """
        Returns the account balance.

        Returns:
            float: The balance of the bank account."
        
        """
        return self.__balance

    @property
    def owner(self) -> str:
        """
        Returns the name of the account owner.

        Returns:
            str: The account owner's name.
        """
                
        return self.__owner

    @property
    def status(self) -> int:
        """
        Returns the account status.

        Returns:
            AccountStatus: The status of the bank account."
        """
        return self.__status

    def update_balance(self, amount: float) -> None:
        """
        Updates the account balance.

        Replaces the current balance with the
        specified amount.

        Args:
            amount (float): The new account balance.
        """
        self.__balance = amount

    def deposit(self, amount: float) -> None:
        """
        Deposits money into the bank account.

        The amount is added to the balance.

        Args:
            amount (float): Amount of money to deposit.
                Must be greater than or equal to zero.

        Raises:
            ValueError: If the amount is negative.
        """

        if amount < 0:
            raise ValueError("amount must be a value greater than or equal to zero.")
        self.__balance += amount

    def withdraw(self, amount):
        """
        Withdraws money from the bank account.

        The amount is subtracted from the balance.

        Args:
            amount (float): Amount of money to withdraw.
                Must be greater than or equal to zero.

        Raises:
            ValueError: If the amount is negative.
            ValueError: If the amount is greater than the
                current account balance.
        """
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
        """
        Returns a string representation of the account.

        Returns:
            str: Account ID, balance, owner, and status.
        """            
        return (f"Account ID: {self.__account_id}\n"
                f"Balance: {self.__balance}\n"
                f"Owner: {self.__owner}\n"
                f"Status: {self.__status}")
    
