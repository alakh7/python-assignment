from datetime import date
from bank_account import BankAccount

class SavingsAccount(BankAccount):
    SERVICE_CHARGE_PREMIUM: float = 2.0  # Flat rate multiplier for service charges when below minimum balance

    def __init__(self, account_number: int, client_number: int, balance: float, date_created: date, minimum_balance):
        super().__init__(account_number, client_number, balance, date_created)
        
        # Validate minimum_balance
        try:
            self._minimum_balance = float(minimum_balance)
        except (ValueError, TypeError):
            self._minimum_balance = 50.0  # Default minimum balance

    def __str__(self) -> str:
        base_info = super().__str__()
        return (
            f"{base_info}\n"
            f"Minimum Balance: ${self._minimum_balance:.2f} Account Type: Savings"
        )

    def get_service_charges(self) -> float:
        if self._balance >= self._minimum_balance:
            return self.BASE_SERVICE_CHARGE
        return self.BASE_SERVICE_CHARGE * self.SERVICE_CHARGE_PREMIUM
