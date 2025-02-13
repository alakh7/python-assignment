import unittest
from datetime import date, timedelta
from investment_account import InvestmentAccount

class TestInvestmentAccount(unittest.TestCase):
    def setUp(self):
        self.ten_years_ago = date.today() - timedelta(days=10 * 365.25)
        self.recent_date = date.today() - timedelta(days=5 * 365.25)
        self.old_date = date.today() - timedelta(days=11 * 365.25)
        
        self.valid_account = InvestmentAccount(123456, 7890, 10000.0, self.recent_date, 3.50)
    
    def test_init_valid_attributes(self):
        print("valid attributes")
        print("----------------------------------------------------")
        print("Actual Account Number: ", self.valid_account.account_number)
        print("Expected Account Number: ", 123456)
        print("Actual Client Number: ", self.valid_account.client_number)
        print("Expected Client Number: ", 7890)
        print("Actual Balance: ", self.valid_account.balance)
        print("Expected Balance: ", 10000.0)
        print("Actual Management Fee: ", self.valid_account._management_fee)
        print("Expected Management Fee: ", 3.50)
        print("\n\n\n")

        self.assertEqual(self.valid_account.account_number, 123456)
        self.assertEqual(self.valid_account.client_number, 7890)
        self.assertEqual(self.valid_account.balance, 10000.0)
        self.assertEqual(self.valid_account._management_fee, 3.50)
    
    def test_init_invalid_management_fee(self):
        account = InvestmentAccount(123456, 7890, 10000.0, self.recent_date, "invalid")
        print("invalid management fee")
        print("----------------------------------------------------")
        print("Actual Management Fee: ", account._management_fee)
        print("Expected Management Fee: ", 2.55)
        print("\n\n\n")
        self.assertEqual(account._management_fee, 2.55)  # Default value
    
    def test_get_service_charges_more_than_10_years(self):
        account = InvestmentAccount(123456, 7890, 10000.0, self.old_date, 3.50)
        print("more than 10 years")
        print("----------------------------------------------------")
        print("Actual Service Charges: ", account.get_service_charges())
        print("Expected Service Charges: ", 4.00)
        print("\n\n\n")

        
        self.assertEqual(round(account.get_service_charges(), 2), 0.50)  # Fee waived
    
    def test_get_service_charges_exactly_10_years(self):
        account = InvestmentAccount(123456, 7890, 10000.0, self.ten_years_ago, 3.50)
        print("exactly 10 years")
        print("----------------------------------------------------")
        print("Actual Service Charges: ", account.get_service_charges())
        print("Expected Service Charges: ", 4.00)
        print("\n\n\n")
        self.assertEqual(round(account.get_service_charges(), 2), 4.00)  # Fee applied
    
    def test_get_service_charges_within_10_years(self):
        print("within 10 years")
        print("----------------------------------------------------")
        print("Actual Service Charges: ", self.valid_account.get_service_charges())
        print("Expected Service Charges: ", 4.0)
        print("\n\n\n")
        self.assertEqual(round(self.valid_account.get_service_charges(), 2), 4.0)  # Fee applied
    
    def test_str_waived_management_fee(self):
        account = InvestmentAccount(123456, 7890, 10000.0, self.old_date, 3.50)
        print("waived management fee")
        print("----------------------------------------------------")
        print("Actual String: ", str(account))
        print("Expected String: ", "Account Number: 123456 Client Number: 7890 Balance: $10000.00 Date Created: 2010-01-01 Management Fee: Waived Account Type: Investment")
        print("\n\n\n")
        self.assertIn("Management Fee: Waived", str(account))
    
    def test_str_display_management_fee(self):
        self.assertIn("Management Fee: $3.50", str(self.valid_account))
    
if __name__ == '__main__':
    unittest.main()
