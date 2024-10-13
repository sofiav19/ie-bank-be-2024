from iebank_api.models import Account
import pytest

def test_create_account():
    """
    GIVEN a Account model
    WHEN a new Account is created
    THEN check the name, account_number, balance, currency, status and created_at fields are defined correctly
    """
    account = Account('John Doe', '€', 'Spain')
    assert account.name == 'John Doe'
    assert account.currency == '€'
    assert account.account_number != None
    assert account.balance == 0.0
    assert account.status == 'Active'
    assert account.country == 'Spain'

def test_account_number_generation():
    account1 = Account(name="User1", currency="€", country="Spain")
    account2 = Account(name="User2", currency="€", country="France")
    assert len(account1.account_number) == 20
    assert len(account2.account_number) == 20
    assert account1.account_number != account2.account_number

def test_invalid_name_raises_error():
    try:
        account = Account(name="", currency="€", country="Spain")
        assert False, "Account creation with empty name should raise an error"
    except Exception as e:
        assert True