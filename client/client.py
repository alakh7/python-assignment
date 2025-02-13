from email_validator import validate_email, EmailNotValidError
 
class Client:
    def __init__(self, client_number: int, first_name: str, last_name: str, email_address: str):
        # Validate client_number
        if not isinstance(client_number, int):
            raise ValueError("client_number must be an integer.")
        self._client_number = client_number
 
        # Validate first_name
        if not first_name.strip():
            raise ValueError("first_name cannot be blank.")
        self._first_name = first_name.strip()
 
        # Validate last_name
        if not last_name.strip():
            raise ValueError("last_name cannot be blank.")
        self._last_name = last_name.strip()
 
        # Validate email_address
        try:
            valid_email = validate_email(email_address)
            self._email_address = valid_email.normalized
        except EmailNotValidError:
            self._email_address = "email@pixell-river.com"
 
    # Property for client_number
    @property
    def client_number(self):
        return self._client_number
 
    # Property for first_name
    @property
    def first_name(self):
        return self._first_name
 
    # Property for last_name
    @property
    def last_name(self):
        return self._last_name
 
    # Property for email_address
    @property
    def email_address(self):
        return self._email_address
 
    # String representation of the class
    def __str__(self):
        return f"{self.last_name}, {self.first_name} [{self.client_number}] - {self.email_address}"
