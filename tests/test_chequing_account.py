
import unittest
from datetime import date

from chequing_account import ChequingAccount

class TestChequingAccount(unittest.TestCase):
    def setUp(self):
        self.valid_account = ChequingAccount(123456, 7890, 500.0, date.today(), -200.0, 0.03)

    def test_init_valid_attributes(self):
        print("Valid Attributes")
        print("------------------------------------------------------------")
        print("Actual Account Number: ",self.valid_account.account_number)
        print("Expected Account Number: ",123456)
        print("Actual Client Number: ",self.valid_account.client_number)
        print("Expected Client Number: ",7890)
        print("Actual Balance: ",self.valid_account.balance)
        print("Expected Balance: ",500.0)
        print("Actual Overdraft Limit: ",self.valid_account._overdraft_limit)
        print("Expected Overdraft Limit: ",-200.0)
        print("Actual Overdraft Rate: ",self.valid_account._overdraft_rate)
        print("Expected Overdraft Rate: ",0.03)
        print("\n\n\n")

        self.assertEqual(self.valid_account.account_number, 123456)
        self.assertEqual(self.valid_account.client_number, 7890)
        self.assertEqual(self.valid_account.balance, 500.0)
        self.assertEqual(self.valid_account._overdraft_limit, -200.0)
        self.assertEqual(self.valid_account._overdraft_rate, 0.03)

    def test_init_invalid_overdraft_limit(self):
        account = ChequingAccount(123456, 7890, 500.0, date.today(), "invalid", 0.03)
        print("Invalid Overdraft Limit")
        print("------------------------------------------------------------")

        print("Actual Overdraft Limit: ",account._overdraft_limit)
        print("Expected Overdraft Limit: ",-100.0)
        print("\n\n\n")

        self.assertEqual(account._overdraft_limit, -100.0)  

    def test_init_invalid_overdraft_rate(self):
        account = ChequingAccount(123456, 7890, 500.0, date.today(), -200.0, "invalid")
        print("Invalid Overdraft Rate")
        print("------------------------------------------------------------")
        print("Actual Overdraft Rate: ",account._overdraft_rate)
        print("Expected Overdraft Rate: ",0.05)
        print("\n\n\n")
        self.assertEqual(account._overdraft_rate, 0.05)  

    def test_init_invalid_date_created(self):
        account = ChequingAccount(123456, 7890, 500.0, "invalid_date", -200.0, 0.03)
        print("Invalid Date Created")
        print("------------------------------------------------------------")
        print("Actual Date Created: ",account._date_created)
        print("Expected Date Created: ",date.today())
        print("\n\n\n")
        self.assertEqual(account._date_created, date.today())  

    def test_get_service_charges_balance_greater_than_overdraft(self):
        print("Charges Balance Greater Than Overdraft")
        print("------------------------------------------------------------")
        print("Actual Balance: ",self.valid_account.get_service_charges())
        print("Expected Balance: ",0.50)
        print("\n\n\n")
        self.assertEqual(self.valid_account.get_service_charges(), 0.50)  

    def test_get_service_charges_balance_less_than_overdraft(self):
        account = ChequingAccount(123456, 7890, -300.0, date.today(), -200.0, 0.03)
        print("Charges Balance Less Than Overdraft")
        print("------------------------------------------------------------")
        print("Actual Balance: ",account.get_service_charges())
        print("Expected Balance: ",0.50 + (100 * 0.03))
        print("\n\n\n")
        expected_charge = 0.50 + (100 * 0.03)
        self.assertEqual(account.get_service_charges(), expected_charge)

    def test_get_service_charges_balance_equal_overdraft(self):
        account = ChequingAccount(123456, 7890, -200.0, date.today(), -200.0, 0.03)
        print("Charges Balance Equal Overdraft")
        print("------------------------------------------------------------")
        print("Actual Balance: ",account.get_service_charges())
        print("Expected Balance: ",0.50)
        print("\n\n\n")
        self.assertEqual(account.get_service_charges(), 0.50) 

    def test_str_representation(self):
        expected_str = (
            f"Account Number: 123456 Balance: $500.00\n"
            f"Overdraft Limit: $-200.00 \nOverdraft Rate: 3.00% \nAccount Type: Chequing"
        )
        self.assertEqual(str(self.valid_account), expected_str)

if __name__ == '__main__':
    unittest.main()