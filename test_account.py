import pytest
from account import *


def test___init__():
    account = Account("John")
    assert account.__account_name == "John"
    assert account.__account_balance == 0


def test_deposit():
    account = Account("John")
    account.deposit(20)
    assert account.__account_balance == 20
    assert account.__account_balance != -20


def test_withdraw():
    account = Account("John")
    account.deposit(20)
    account.withdraw(10)
    assert account.__account_balance == 10
    assert account.__account_balance != -10
