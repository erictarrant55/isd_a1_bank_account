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

        self.__client_id = client_id
        self.__name = name
        self.__email_address = email_address
        
