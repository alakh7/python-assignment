

"""
Description: A client program written to verify correctness of 
the BankAccount sub-classes.
"""
__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = ""




#     Import date from datetime
from datetime import date

# 1.  Import all Bank Acount types using the bank_account package
from tests.chequing_account import ChequingAccount
from tests.savings_account import SavingsAccount
from tests.investment_account import InvestmentAccount

# 2. Create an instance of a ChequingAccount with values of your 
# choice including a balance which is below the overdraft limit.
chequing_account = ChequingAccount(123456, 1001, -250.0, date.today(), -200.0, 0.05)

# 3. Print the ChequingAccount created in step 2.
print("=========================== Chequing Account with balance below overdraft limit ================================")
print(chequing_account)
print("\n\n")
# 3b. Print the service charges amount if calculated based on the current state of the ChequingAccount created in step 2.
print("Service Charges for Chequing Account with balance below overdraft limit:", chequing_account.get_service_charges())
print("\n\n")
    
# 4a. Deposit enough money to avoid overdraft fees.
try:
    chequing_account.deposit(150.0)
except Exception as e:
    print("Error:", e)

# 4b. Print the ChequingAccount
print("Updated Chequing Account after adding money to avoid overdraft fees:")
print(chequing_account)
print("\n\n\n")

# 4c. Print the service charges amount
print("Service Charges for Chequing Account with balance above overdraft limit:", chequing_account.get_service_charges())
print("===================================================")

print("\n\n\n")
# 5. Create an instance of a SavingsAccount with a balance above the minimum balance.
savings_account = SavingsAccount(789123, 1002, 200.0, date.today(), 50.0)

# 6. Print the SavingsAccount
print("=========================== Savings Account with balance above minimum balance ================================")
print(savings_account)

# 6b. Print the service charges amount
print("Service Charges for Saving Account with amount above minimum balance:", savings_account.get_service_charges())
print("\n\n\n")

# 7a. Withdraw enough money to drop below the minimum balance.

print("Withdrawing $160.0 from Savings Account ...")
try:
    savings_account.withdraw(160.0)
except Exception as e:
    print("Error:", e)
print("\n")
# 7b. Print the SavingsAccount
print("Updated Savings Account after balance falls below minimum balance:")
print(savings_account)

# 7c. Print the service charges amount
print("Service Charge for Savings Account after withdrawal (with balance below minimum balance):")
print(savings_account.get_service_charges())

print("===================================================")
print("\n\n\n")

# 8. Create an InvestmentAccount instance with a date created within the last 10 years.
investment_account_recent = InvestmentAccount(654321, 1003, 5000.0, date.today(), 3.00)

# 9a. Print the InvestmentAccount
print("=========================== Investment Account created within the last 10 years ================================")
print(investment_account_recent)
print("\n\n\n")

# 9b. Print the service charges amount
print("Service Charges for Investment Account:", investment_account_recent.get_service_charges())

# 10. Create an InvestmentAccount instance with a date created prior to 10 years ago.

investment_account_old = InvestmentAccount(987654, 1004, 7000.0, date.today().replace(year=date.today().year - 11), 3.00)

# 11a. Print the InvestmentAccount
print("=========================== Investment Account Older than 10 years ================================")
print(investment_account_old)

# 11b. Print the service charges amount
print("Service Charges for Investment Account more than 10 years old:", investment_account_old.get_service_charges())

print("===================================================")
print("\n\n\n")

# 12. Withdraw service charges from each account.
print("Withdrawing service charges from each account")
for account in [chequing_account, savings_account, investment_account_recent, investment_account_old]:
    try:
        print(f"Withdrawing service charges from {type(account).__name__}")
        account.withdraw(account.get_service_charges())
    except Exception as e:
        print(f"Error withdrawing from {type(account).__name__}:", e)
print("\n\n\n")

# 13. Print all updated bank account objects.
print("Updated Bank Accounts:")
for account in [chequing_account, savings_account, investment_account_recent, investment_account_old]:
    print(account)
