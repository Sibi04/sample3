import pytest
from project import Account, SavingsAccount, CurrentAccount  # Import classes from new.py

def test_deposit():
    acc = Account("12345", 1000)
    result = acc.deposit(500)
    assert acc.balance == 1500
    assert result == "Deposited 500. New balance: 1500"

def test_withdraw():
    acc = Account("12345", 1000)
    result = acc.withdraw(500)
    assert acc.balance == 500
    assert result == "Withdrew 500. New balance: 500"

def test_withdraw_insufficient_funds():
    acc = Account("12345", 1000)
    result = acc.withdraw(2000)
    assert result == "Insufficient funds"

def test_add_interest():
    savings = SavingsAccount("12345", 1000, 5)
    result = savings.add_interest()
    assert savings.balance == 1050
    assert "Interest added" in result

def test_current_account_overdraft():
    current = CurrentAccount("67890", 2000, 500)
    result = current.withdraw(2500)
    assert current.balance == -500
    assert "Withdrew 2500" in result

def test_current_account_exceed_overdraft():
    current = CurrentAccount("67890", 2000, 500)
    result = current.withdraw(3000)
    assert result == "Exceeded overdraft limit"