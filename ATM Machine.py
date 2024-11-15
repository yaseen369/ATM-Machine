class Bank:
    """Handles customers, ATMs, and overall bank operations."""
    def __init__(self, name):
        self.name = name
        self.customers = {}
        self.atms = []

    def add_customer(self, customer):
        self.customers[customer.customer_id] = customer
        print(f"Welcome {customer.name}! You are now part of {self.name}.")

    def add_atm(self, atm):
        self.atms.append(atm)
        print(f"New ATM added with ${atm.cash_available} cash.")

    def get_customer(self, customer_id):
        return self.customers.get(customer_id)

    def display_customers(self):
        print(f"{self.name} Customers:")
        for customer in self.customers.values():
            print(f"- {customer.name} (ID: {customer.customer_id})")


class Customer:
    """Manages customer details and account interactions."""
    def __init__(self, customer_id, name, account):
        self.customer_id = customer_id
        self.name = name
        self.account = account

    def withdraw(self, atm, amount):
        print(f"{self.name} is attempting to withdraw ${amount}...")
        transaction = Transaction(self.account, atm)
        return transaction.process(amount)


class Account:
    """Stores account balance and withdrawal limits."""
    def __init__(self, account_id, balance, daily_limit):
        self.account_id = account_id
        self.balance = balance
        self.daily_limit = daily_limit

    def can_withdraw(self, amount):
        return self.balance >= amount and amount <= self.daily_limit

    def withdraw(self, amount):
        if self.can_withdraw(amount):
            self.balance -= amount
            return True
        return False


class ATM:
    """Simulates an ATM with cash availability."""
    def __init__(self, cash_available):
        self.cash_available = cash_available

    def can_dispense(self, amount):
        return self.cash_available >= amount

    def dispense(self, amount):
        if self.can_dispense(amount):
            self.cash_available -= amount
            print(f"${amount} dispensed. Please collect your cash.")
            return True
        print("ATM Error: Insufficient funds.")
        return False


class Transaction:
    """Manages withdrawals and ensures proper checks."""
    def __init__(self, account, atm):
        self.account = account
        self.atm = atm

    def process(self, amount):
        if not self.account.can_withdraw(amount):
            print("Transaction failed: Check balance or daily limit.")
            return False
        if not self.atm.can_dispense(amount):
            print("Transaction failed: ATM has insufficient cash.")
            return False
        if self.account.withdraw(amount):
            if self.atm.dispense(amount):
                print("Withdrawal successful.")
                return True
            else:
                print("Transaction canceled: Cash dispense failed.")
                self.account.balance += amount
        return False

