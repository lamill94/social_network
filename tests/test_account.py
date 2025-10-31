from lib.account import Account

# Test account constructs

def test_account_constructs():
    account = Account(1, 'laurenm@gmail.com', 'lamill94')
    assert account.id == 1
    assert account.email == 'laurenm@gmail.com'
    assert account.username == 'lamill94'

# Compare two identical accounts and have them be equal

def test_accounts_are_equal():
    account1 = Account(1, 'laurenm@gmail.com', 'lamill94')
    account2 = Account(1, 'laurenm@gmail.com', 'lamill94')
    assert account1 == account2

# Test that account can be formatted nicely

def test_account_formats_nicely():
    account = Account(1, 'laurenm@gmail.com', 'lamill94')
    assert str(account) == "Account(1, laurenm@gmail.com, lamill94)"