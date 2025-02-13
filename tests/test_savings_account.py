import unittest
from datetime import date
from savings_account import SavingsAccount

class TestSavingsAccount(unittest.TestCase):
    def setUp(self):
        self.valid_account = SavingsAccount(123456, 7890, 500.0, date.today(), 50.0)
    
    def test_init_valid_attributes(self):
        print("Valid Attributes")
        print("----------------------------------------------------")
        print(f"Account Number: {self.valid_account.account_number}")
        print("Expected Account Number: 123456")
        print(f"Client Number: {self.valid_account.client_number}")
        print("Expected Client Number: 7890")
        print(f"Balance: {self.valid_account.balance}")
        print("Expected Balance: 500.0")    
        print(f"Minimum Balance: {self.valid_account._minimum_balance}")
        print("Expected Minimum Balance: 50.0")
        print("\n\n\n")
        self.assertEqual(self.valid_account.account_number, 123456)
        self.assertEqual(self.valid_account.client_number, 7890)
        self.assertEqual(self.valid_account.balance, 500.0)
        self.assertEqual(self.valid_account._minimum_balance, 50.0)
    
    def test_init_invalid_minimum_balance(self):
        account = SavingsAccount(123456, 7890, 500.0, date.today(), "invalid")
        print("Invalid Minimum Balance")
        print("----------------------------------------------------")
        print("Actual Minimum Balance: ", account._minimum_balance)
        print("Expected Minimum Balance: 50.0")
        print("\n\n\n")
        self.assertEqual(account._minimum_balance, 50.0)  # Default value
    
    def test_get_service_charges_greater_than_minimum_balance(self):
        print("Greater Than Minimum Balance")

        print("----------------------------------------------------")
        print("Actual Service Charge: ", self.valid_account.get_service_charges())
        print("Expected Service Charge: 0.50")
        print("\n\n\n")        
        self.assertEqual(round(self.valid_account.get_service_charges(), 2), 0.50)
    
    def test_get_service_charges_equal_to_minimum_balance(self):
        account = SavingsAccount(123456, 7890, 50.0, date.today(), 50.0)
        print("Equal To Minimum Balance")
        print("----------------------------------------------------")
        print("Actual Service Charge: ", account.get_service_charges())
        print("Expected Service Charge: 0.50")
        print("\n\n\n")
        self.assertEqual(round(account.get_service_charges(), 2), 0.50)
    
    def test_get_service_charges_less_than_minimum_balance(self):
        account = SavingsAccount(123456, 7890, 49.99, date.today(), 50.0)
        print("Less Than Minimum Balance")
        print("----------------------------------------------------")
        print("Actual Service Charge: ", account.get_service_charges())
        print("Expected Service Charge: 1.00")
        print("\n\n\n")
        self.assertEqual(round(account.get_service_charges(), 2), 1.00)  # Service charge premium applies
    
    def test_str_representation(self):
        expected_str = (
            f"Account Number: 123456 Balance: $500.00\n"
            f"Minimum Balance: $50.00 Account Type: Savings"
        )
        self.assertEqual(str(self.valid_account), expected_str)
    
if __name__ == '__main__':
    unittest.main()