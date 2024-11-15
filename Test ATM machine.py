# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 18:57:04 2024

@author: yasee
"""

def test_withdrawal():
    # create acc
    account = Account(account_id="12345", balance=500, daily_withdrawal_limit=300)

    # Create a Customer linked to the account
    customer = Customer(customer_id="C001", name="Alice", account=account)

    # Create an ATM with a set cash reserve
    atm = ATM(cash_available=1000)

    # Test Cases
    print("Test 1: Valid withdrawal within balance and limit")
    print("Expected: Transaction successful.")
    customer.request_withdrawal(atm, 200)

    print("\nTest 2: Exceeds daily withdrawal limit")
    print("Expected: Transaction failed due to daily limit.")
    customer.request_withdrawal(atm, 400)

    print("\nTest 3: Insufficient account balance")
    print("Expected: Transaction failed due to insufficient balance.")
    customer.request_withdrawal(atm, 600)

    print("\nTest 4: ATM has insufficient cash")
    # Temporarily reduce ATM's cash to test the insufficient cash scenario
    atm.cash_available = 100
    print("Expected: Transaction failed due to insufficient ATM cash.")
    customer.request_withdrawal(atm, 200)

    # Reset ATM's cash for further tests
    atm.cash_available = 1000

    print("\nTest 5: Exact daily limit withdrawal")
    print("Expected: Transaction successful, at daily limit.")
    customer.request_withdrawal(atm, 300)


# Run the test
test_withdrawal()
