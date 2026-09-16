from account.account_status import AccountStatus
from email_validator import validate_email, EmailNotValidError

class Client:
    def __init__(
            self,
            client_id,
            name,
            email_address):
        """Represents the client profile."""
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
        return self.__client_id
    @property 
    def name(self):
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