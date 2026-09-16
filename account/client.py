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
            raise ValueError("name must not be empty.")
        if len(email_address.strip()) <= 0:
            raise ValueError("email_address must not be empty.")
        self.__client_id = client_id
        self.__name = name
        self.__email_address = email_address
    @property
    def client_id(self) -> int:
        return self.client_id

    @property 
    def name(self) -> str:
        return self.name

    @property
    def email_address(self) -> str:
        return self.email_address
    @email_address.setter
    def email_address(self, email_address: str) -> None:
        email_address = email_address.strip()

        email = validate_email(
            email_address,
            check_deliverability=False
            )
        self.__email_address = email.normalized

    def __str__(self) -> str:
                return (f"Client ID: {self.__client_id}\n"
                        f"Name: {self.__name}\n"
                        f"Email Address: {self.__email_address}")

    

