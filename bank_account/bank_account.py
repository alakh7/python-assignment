from datetime import date
from abc import ABC, abstractmethod


class BankAccount(ABC):
    BASE_SERVICE_CHARGE: float = 0.50  # Base service charge applicable to all accounts

    def __init__(self, account_number: int, client_number: int, balance: float, date_created: date):
        # Validate and set account number
        if not isinstance(account_number, int):
            raise ValueError("Account number must be an integer.")
        self._account_number = account_number

        # Validate and set client number
        if not isinstance(client_number, int):
            raise ValueError("Client number must be an integer.")
        self._client_number = client_number

        # Validate and set balance, default to 0.0 if invalid
        try:
            self._balance = float(balance)
        except ValueError:
            self._balance = 0.0

        # Validate date_created, default to today's date if invalid
        self._date_created = date_created if isinstance(date_created, date) else date.today()

    @property
    def account_number(self) -> int:
        return self._account_number

    @property
    def client_number(self) -> int:
        return self._client_number

    @property
    def balance(self) -> float:
        return self._balance

    def update_balance(self, amount: float) -> None:
        # Update balance after validating amount
        try:
            self._balance += float(amount)
        except ValueError:
            raise ValueError("Amount must be numeric.")

    def deposit(self, amount: float) -> None:
        # Validate deposit amount
        if not isinstance(amount, (int, float)):
            raise ValueError("Deposit amount must be numeric.")
        if amount <= 0:
            raise ValueError(f"Deposit amount: {amount:.2f} must be positive.")
        self.update_balance(amount)

    def withdraw(self, amount: float) -> None:
        # Validate withdrawal amount and check balance
        if not isinstance(amount, (int, float)):
            raise ValueError("Withdraw amount must be numeric.")
        if amount <= 0:
            raise ValueError(f"Withdraw amount: {amount:.2f} must be positive.")
        if amount > self._balance:
            raise ValueError(f"Withdraw amount: {amount:.2f} must not exceed the account balance: {self._balance:.2f}.")
        self.update_balance(-amount)

    def __str__(self) -> str:
        # Return a string representation of the account
        return f"Account Number: {self._account_number} Balance: ${self._balance:,.2f}"

    @abstractmethod
    def get_service_charges(self) -> float:
        # Abstract method to be implemented by subclasses
        pass
