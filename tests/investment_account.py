from datetime import date, timedelta
from .bank_account import BankAccount

class InvestmentAccount(BankAccount):
    TEN_YEARS_AGO: date = date.today() - timedelta(days=10 * 365.25)

    def __init__(self, account_number: int, client_number: int, balance: float, date_created: date, management_fee):
        super().__init__(account_number, client_number, balance, date_created)
        
        # Validate management_fee
        try:
            self._management_fee = float(management_fee)
        except (ValueError, TypeError):
            self._management_fee = 2.55  # Default management fee

    def __str__(self) -> str:
        base_info = super().__str__()
        
        if self._date_created > self.TEN_YEARS_AGO:
            management_fee_str = f"${self._management_fee:.2f}"
        else:
            management_fee_str = "Waived"
        
        return (
            f"{base_info}\n"
            f"Date Created: {self._date_created} Management Fee: {management_fee_str} Account Type: Investment"
        )

    def get_service_charges(self) -> float:
        if self._date_created >= self.TEN_YEARS_AGO:
            return 0.50 + self._management_fee
        return 0.50
