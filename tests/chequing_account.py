from datetime import date

from .bank_account import BankAccount

class ChequingAccount(BankAccount):
    def __init__(self, account_number: int, client_number: int, balance: float, date_created: date, overdraft_limit, overdraft_rate):
        super().__init__(account_number, client_number, balance, date_created)

        # Validate overdraft limit
        try:
            self._overdraft_limit = float(overdraft_limit)
        except (ValueError, TypeError):
            self._overdraft_limit = -100.0  # Default overdraft limit

        # Validate overdraft rate
        try:
            self._overdraft_rate = float(overdraft_rate)
        except (ValueError, TypeError):
            self._overdraft_rate = 0.05  # Default overdraft rate

    def __str__(self) -> str:
        return (
            f"{super().__str__()}\n"
            f"Overdraft Limit: ${self._overdraft_limit:,.2f} \nOverdraft Rate: {self._overdraft_rate * 100:.2f}% \nAccount Type: Chequing"
        )

    def get_service_charges(self) -> float:
        if self._balance >= self._overdraft_limit:
            return self.BASE_SERVICE_CHARGE
        else:
            return self.BASE_SERVICE_CHARGE + (self._overdraft_limit - self._balance) * self._overdraft_rate
