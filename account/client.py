from account.account_status import AccountStatus
from email_validator import validate_email

__author__ = "Eric Tarrant"
__version__ = "1.0.0"


class Client:
    """
    Represents the client's profile.

    Attributes:
        client_id (int): The identifier for the client.
        name (str): The name of the client.
        email_address (str): The normalized email address of the client.
    """

    def __init__(self, client_id: int, name: str, email_address: str):
        """
        Represents a new Client profile.

        Args:
            client_id (int): The identifier for the client.
                Must be greater than zero.
            name (str): The name of the client. Cannot be empty.
            email_address (str): The client's email address.

        Raises:
            ValueError: If client_id is less than or equal to zero.
            ValueError: If name is empty or only whitespace.
            EmailNotValidError: If email_address is not a valid
                email address.
        """
        if client_id <= 0:
            raise ValueError("client_id must be a value greater than zero.")

        name = name.strip()
        if len(name) == 0:
            raise ValueError("name cannot be an empty string.")

        self.__client_id = client_id
        self.__name = name
        # Reuse the setter so validation and normalization live in one place.
        self.email_address = email_address

    @property
    def client_id(self) -> int:
        """Returns the client's ID."""
        return self.__client_id

    @property
    def name(self) -> str:
        """Returns the client's name."""
        return self.__name

    @property
    def email_address(self) -> str:
        """Returns the client's normalized email address."""
        return self.__email_address

    @email_address.setter
    def email_address(self, email_address: str) -> None:
        """
        Validates and updates the client's email address.

        Raises:
            EmailNotValidError: If the email address is not valid.
        """
        email = validate_email(
            email_address.strip(),
            check_deliverability=False
        )
        self.__email_address = email.normalized

    def __str__(self) -> str:
        """
        Returns a string representation of the client.

        Returns:
            str: Formatted as "<name> [<client_id>] - <email_address>".
        """
        return f"{self.__name} [{self.__client_id}] - {self.__email_address}"