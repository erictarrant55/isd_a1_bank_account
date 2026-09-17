from account.account_status import AccountStatus
from email_validator import validate_email, EmailNotValidError

class Client:
    """
    Represents the client's profile.

    The Client class stores the information about a client, which includes
    the client ID, name, and email address.

    Attributes:
        client_id (int): The identifier for the client.
        name (str): The name of the client.
        email_address (str): the email address that is associated
        with the client.

    Raises:
        ValueError: If client_id is less than or equal to zero.
        ValueError: If name is empty or contains only whitespace.
        ValueError: If email_address is empty or contains only whitespace.
        ValueError: If email_address is not a valid email address.
    """
    def __init__(
            self,
            client_id,
            name,
            email_address):
        """
        Represents a new Client profile.

        Args:
            client_id (int): The identifier for the client.
                Must be greater than zero.
            name (str): The name of the client. Cannot be empty.
            email_address (str): The client's email address. Must be
                a valid and non-empty email address.

        Raises:
            ValueError: If client_id is less than or equal to zero.
            ValueError: If name is empty or contains only whitespace.
            ValueError: If email_address is empty or contains only
                whitespace.
            ValueError: If email_address is not a valid email address.
        """
        if client_id <= 0:
            raise ValueError("client_id must be a value greater than zero.")
        if len(name.strip()) <= 0:
            raise ValueError("name cannot be an empty string.")
        if len(email_address.strip()) <= 0:
            raise ValueError("email_address must not be empty.")
        validate_email(email_address)

        self.__client_id = client_id
        self.__name = name
        self.__email_address = email_address

    @property
    def client_id(self):
        """
        Returns the client's ID.

        Returns:
            int: The unique identifier of the client.
        """
        return self.__client_id
    @property 
    def name(self):
        """
        Returns the client's name.

        Returns:
            str: The name of the client.
        """
        return self.__name

    @property
    def email_address(self):

        return self.__email_address
    
    @email_address.setter
    def email_address(self, email_address: str) -> None:
        email_address = email_address.strip()

        email = validate_email(
            email_address,
            check_deliverability=False
        )
        self.__email_address = email.normalized

    def __str__(self) -> str:
        return f"{self.__name} [{self.__client_id}] - {self.__email_address}"