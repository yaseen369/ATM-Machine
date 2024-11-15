# Bank System Simulation

This is a simple simulation of a bank system, including customers, accounts, ATMs, and transactions. The system allows customers to interact with their accounts, perform withdrawals via ATMs, and handles different checks for account balance, daily withdrawal limits, and ATM cash availability.

## Table of Contents
- [Classes Overview](#classes-overview)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [License](#license)

## Classes Overview

### `Bank`
The `Bank` class manages the overall bank operations, including customers and ATMs.

- **Attributes:**
  - `name` (str): The name of the bank.
  - `customers` (dict): A dictionary holding customer data, indexed by their `customer_id`.
  - `atms` (list): A list of ATMs associated with the bank.

- **Methods:**
  - `add_customer(customer)`: Adds a customer to the bank.
  - `add_atm(atm)`: Adds an ATM to the bank.
  - `get_customer(customer_id)`: Retrieves a customer by their ID.
  - `display_customers()`: Displays all customers of the bank.

### `Customer`
The `Customer` class handles customer data and interactions with their account.

- **Attributes:**
  - `customer_id` (str): A unique identifier for the customer.
  - `name` (str): The name of the customer.
  - `account` (Account): The customer's bank account.

- **Methods:**
  - `withdraw(atm, amount)`: Initiates a withdrawal request using an ATM.

### `Account`
The `Account` class handles the customer's account balance and withdrawal limits.

- **Attributes:**
  - `account_id` (str): A unique identifier for the account.
  - `balance` (float): The current balance of the account.
  - `daily_limit` (float): The maximum amount that can be withdrawn in a single day.

- **Methods:**
  - `can_withdraw(amount)`: Checks if the account has enough balance and if the withdrawal is within the daily limit.
  - `withdraw(amount)`: Performs a withdrawal if possible.

### `ATM`
The `ATM` class simulates an ATM that dispenses cash to customers.

- **Attributes:**
  - `cash_available` (float): The amount of cash available in the ATM.

- **Methods:**
  - `can_dispense(amount)`: Checks if the ATM has enough cash to dispense the requested amount.
  - `dispense(amount)`: Dispenses the specified amount if available.

### `Transaction`
The `Transaction` class handles the logic of processing a withdrawal.

- **Attributes:**
  - `account` (Account): The account from which the withdrawal will be made.
  - `atm` (ATM): The ATM that will dispense the cash.

- **Methods:**
  - `process(amount)`: Manages the withdrawal process, ensuring all checks (balance, daily limit, ATM availability) are passed before completing the transaction.

## Usage

### Step 1: Create a Bank
```python
bank = Bank("MyBank")
```


### Step 2: Create Customers and Accounts

To create customers and accounts, instantiate the `Account` and `Customer` classes. The `Account` class requires an account ID, balance, and daily withdrawal limit. Once the account is created, you can create a customer and associate it with the account.

```python
account1 = Account(account_id="12345", balance=1000, daily_limit=500)
customer1 = Customer(customer_id="1", name="Alice", account=account1)

# Add customer to the bank
bank.add_customer(customer1)
```
### Step 3: Create ATMs and Add Them to the Bank

In this step, you create an ATM and add it to the bank's list of ATMs. The `ATM` class requires the amount of cash available in the ATM. Once the ATM is created, you can add it to the bank using the `add_atm` method.

```python
atm1 = ATM(cash_available=2000)

# Add ATM to the bank
bank.add_atm(atm1)
```

### Step 4: Withdraw Money

To initiate a withdrawal, use the `withdraw` method on the `customer` object, specifying the ATM and the withdrawal amount. The system will perform various checks (such as balance, daily withdrawal limit, and ATM cash availability) before processing the withdrawal.

```python
customer1.withdraw(atm1, 300)
```

## Dependencies
This project does not require any external dependencies. It can be run with any Python 3.x interpreter.


## Acknowledgments

This project was created as part of a school assignment for the Software Design and Architecture course at Near East University. Special thanks to Instructor Priscilla for her guidance and support throughout the project.


