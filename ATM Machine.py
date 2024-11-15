class Bank:
    """
    A bank that manages customers, accounts, and ATMs.
    """
    def __init__(self, name):
        self.name = name
        self.customers = {}
        self.atms = []

    def add_customer(self, customer):
        """Adds a customer to the bank."""
        self.customers[customer.customer_id] = customer
        print(f"Customer '{customer.name}' added to {self.name}.")

    def add_atm(self, atm):
        """Adds an ATM to the bank."""
        self.atms.append(atm)
        print(f"ATM with cash ${atm.cash_available} added to {self.name}.")

    def find_customer_by_id(self, customer_id):
        """Finds and returns a customer by their ID."""
        return self.customers.get(customer_id, None)

    def list_customers(self):
        """Lists all customers in the bank."""
        print(f"Customers in {self.name}:")
        for customer in self.customers.values():
            print(f"- {customer.name} (ID: {customer.customer_id})")


class Customer:
    """
    Links to their bank account to manage balance and withdrawal limits.
    """
    def __init__(self, customer_id, name, account):
        self.customer_id = customer_id
        self.name = name
        self.account = account

    def request_withdrawal(self, atm, amount):
        """Requests a cash withdrawal by interacting with an ATM."""
        print(f"{self.name} (Customer ID: {self.customer_id}) is requesting a withdrawal of ${amount}.")
        transaction = Transaction(self.account, atm)
        result = transaction.process_withdrawal(amount)
        return result


class Account:
    """Represents a bank account with a balance and daily withdrawal limit."""
    def __init__(self, account_id, balance, daily_withdrawal_limit):
        self.account_id = account_id
        self.balance = balance
        self.daily_withdrawal_limit = daily_withdrawal_limit

    def has_sufficient_balance(self, amount):
        return self.balance >= amount

    def within_daily_limit(self, amount):
        return amount <= self.daily_withdrawal_limit

    def deduct_balance(self, amount):
        if self.has_sufficient_balance(amount) and self.within_daily_limit(amount):
            self.balance -= amount
            return True
        return False


class ATM:
    """Represents an ATM with cash available for dispensing."""
    def __init__(self, cash_available):
        self.cash_available = cash_available

    def has_sufficient_cash(self, amount):
        return self.cash_available >= amount

    def dispense_cash(self, amount):
        if self.has_sufficient_cash(amount):
            self.cash_available -= amount
            print(f"Dispensing ${amount}. Please take your cash.")
            return True
        else:
            print("Sorry, this ATM doesn’t have enough cash.")
            return False


class Transaction:
    """
    Verifies account balance, checks ATM cash, and processes the transaction.
    """
    def __init__(self, account, atm):
        self.account = account
        self.atm = atm

    def process_withdrawal(self, amount):
        print(f"Processing a withdrawal request for ${amount}...")

        if not self.account.has_sufficient_balance(amount):
            result = False
            print("Failed: Not enough funds in the account.")
            return result

        if not self.account.within_daily_limit(amount):
            result = False
            print("Failed: This amount exceeds the daily withdrawal limit.")
            return result

        if not self.atm.has_sufficient_cash(amount):
            result = False
            print("Failed: ATM doesn’t have enough cash available.")
            return result

        if self.account.deduct_balance(amount):
            cash_dispensed = self.atm.dispense_cash(amount)
            if cash_dispensed:
                result = True
                print("Success! Transaction complete.")
            else:

                self.account.balance += amount
                result = False
                print("Failed: Could not dispense cash, transaction canceled.")
        else:
            result = False
            print("Failed: Could not deduct amount from the account.")


        return result


