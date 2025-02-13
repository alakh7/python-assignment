# Intermediate Software Development Automated Teller Project
This project will be developed over the course of several assignments.  Each assignment will build on the work done in the previous assignment(s).  Ultimately, an entire system will be created to manage bank transactions for clients who have one or more bank accounts.

## Author
Manjot Kaur

## Assignment
Assignment [1]: [The assignment is related classes, unit testing, Accessors, Mutators and more.]

## Encapsulation
[use this section to explain how Encapsulation was achieved in the BankAccount class.]
Encapsulation in the BankAccount and Transaction classes works as follows:

Private Attributes: Key attributes like _balance and _transaction_id are kept private to prevent unauthorized access.
Access Methods: Getters and setters offer controlled interaction with these attributes, ensuring secure and validated changes.
Data Validation: Methods such as deposit() and withdraw() implement safeguards to preserve data accuracy and integrity.
Advantages: Encapsulation shields the data, ensures reliability, and hides the complexity of the implementation, making the classes more robust and easier to manage.




## Assignment
Assignment [2]: [This assignment focuses on inheritance, polymorphism, unit testing, and enhancing the BankAccount hierarchy with specialized account types.]

## Inheritance & Polymorphism
[Use this section to explain how inheritance and polymorphism were applied in the BankAccount subclasses.]

- **Inheritance:** The `ChequingAccount`, `SavingsAccount`, and `InvestmentAccount` classes inherit from the `BankAccount` class, reusing common attributes and methods while introducing account-specific functionality.
- **Polymorphism:** The `get_service_charges()` method is overridden in each subclass to apply distinct service charge rules based on the account type.
- **Encapsulation:**
  - Private attributes such as `_balance`, `_minimum_balance`, and `_overdraft_limit` ensure restricted access and maintain data integrity.
  - Controlled interaction is achieved using accessors and mutators (getters and setters), ensuring secure attribute modifications.
  - Methods like `deposit()`, `withdraw()`, and `update_balance()` enforce transaction validation, preventing invalid operations.

## Advantages
- **Code Reusability:** The use of inheritance reduces code duplication by centralizing common logic in the `BankAccount` class.
- **Extensibility:** New account types can be added with minimal modifications to the existing codebase.
- **Robustness:** Encapsulation ensures better data security and prevents unintended modifications, while polymorphism enhances flexibility by allowing different implementations of `get_service_charges()`.
- **Unit Testing:** The implementation includes extensive unit tests verifying correct behavior for initialization, service charge calculations, and string representations of different account types.

This assignment further strengthens the design of the Automated Teller Project by enhancing modularity, maintainability, and accuracy in financial transactions.
