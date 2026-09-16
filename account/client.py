from account.account_status import AccountStatus

class Client:
    def __init__(
            self,
            client_id,
            name,
            email_address):
        """Represents the client profile."""
        if len(client_id.strip()) <= 0:
            raise ValueError("client_id must be a value greater than zero.")
        if name == len(""):
            raise ValueError("name cannot be an empty string.") 
        # if not isinstance(email_address, int):
        #     raise ValueError(validate_email)
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

    def __str__(self) -> str:
                return (f"Client ID: {self.__client_id()}\n"
                        f"Name: {self.__name()}\n"
                        f"Email Address: {self.__email_address()}")

    #def validate_email():

