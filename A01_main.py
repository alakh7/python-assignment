""""
Description: A client program written to verify correctness of 
the BankAccount and Client classes.
"""
__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Manjot Kaur"

from bank_account.bank_account import BankAccount
from client.client import Client

def main():
    """Test the functionality of the methods encapsulated 
    in the BankAccount and Client classes.
    """ 
    # In the statements coded below, ensure that any statement that could result 
    # in an exception is handled.  When exceptions are 'caught', display the exception 
    # message to the console.

    # 1. Code a statement which creates a valid instance of the Client class.
    # Use your own unique valid values for the inputs to the class.
    try:
        client = Client(client_number=67890, name="John Doe", address="123 Main St")
        print(f"Client created successfully: {client}")
    except Exception as e:
        print(f"Error creating Client: {e}")
 
    # 2. Declare a BankAccount object with an initial value of None.
    bank_account = None
 
    # 3. Using the bank_account object declared in step 2, code a statement 
    # to instantiate the BankAccount object.
    # Use any integer value for the BankAccount number.
    # Use the client_number used to create the Client object in step 1 for the 
    # BankAccount's client_number. 
    # Use a floating point value for the balance. 
    try:
        bank_account = BankAccount(account_number=12345, client_number=client.client_number, balance=100.0)
        print(f"BankAccount created successfully: {bank_account}")
    except Exception as e:
        print(f"Error creating BankAccount: {e}")


    # 4. Code a statement which creates an instance of the BankAccount class.
    # Use an INVALID value (non-float) for the balance. 
    # Use any integer value for the BankAccount number.
    # Use the client_number used to create the Client object in step 1 for the 
    # BankAccount's client_number. 
    # Use an INVALID value (non-float) for the balance. 
    try:
        invalid_bank_account = BankAccount(account_number=54321, client_number=client.client_number, balance="InvalidBalance")
    except Exception as e:
        print(f"Error creating BankAccount with invalid balance: {e}")

    # 5. Code a statement which prints the Client instance created in step 1. 
    # Code a statement which prints the BankAccount instance created in step 3.
    print(f"Client: {client}")
    print(f"BankAccount: {bank_account}")

    # 6. Attempt to deposit a non-numeric value into the BankAccount create in step 3. 
    try:
        bank_account.deposit("InvalidDeposit")
    except Exception as e:
        print(f"Error during deposit of non-numeric value: {e}")

    # 7. Attempt to deposit a negative value into the BankAccount create in step 3. 
    try:
        bank_account.deposit(-50.0)
    except Exception as e:
        print(f"Error during deposit of negative value: {e}")
 
    # 8. Attempt to withdraw a valid amount of your choice from the BankAccount create in step 3. 
    try:
        bank_account.withdraw(50.0)
        print(f"Withdrawal successful. Updated balance: {bank_account.balance}")
    except Exception as e:
        print(f"Error during valid withdrawal: {e}")

    # 9. Attempt to withdraw a non-numeric value from the BankAccount create in step 3. 
    try:
        bank_account.withdraw("InvalidWithdraw")
    except Exception as e:
        print(f"Error during withdrawal of non-numeric value: {e}")

    # 10. Attempt to withdraw a negative value from the BankAccount create in step 3. 
    try:
        bank_account.withdraw(-30.0)
    except Exception as e:
        print(f"Error during withdrawal of negative value: {e}")

    # 11. Attempt to withdraw a value from the BankAccount create in step 3 which 
    # exceeds the current balance of the account. 
    try:
        bank_account.withdraw(200.0)  # Assuming balance is now less than $200 after previous operations
    except Exception as e:
        print(f"Error during withdrawal exceeding balance: {e}")

    # 12. Code a statement which prints the BankAccount instance created in step 3. 
    print(f"Final BankAccount state: {bank_account}")
 
if __name__ == "__main__":
    main()
  