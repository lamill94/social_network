from lib.account_repository import AccountRepository
from lib.account import Account

# When we call all method
# We get a list of Account objects reflecting the seed data

def test_get_all_records(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = AccountRepository(db_connection)

    accounts = repository.all()

    assert accounts == [
        Account(1, 'laurenm@gmail.com', 'lamill94'),
        Account(2, 'claudiom@gmail.com', 'claudioAudio'),
        Account(3, 'stinkylara@gmail.com', 'IStinkNice')
    ]

# When we call create method
# We get a new record in the database

def test_create_record(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = AccountRepository(db_connection)
    repository.create(Account(None, 'newemail.com', 'NewUsername'))

    accounts = repository.all()

    assert accounts == [
        Account(1, 'laurenm@gmail.com', 'lamill94'),
        Account(2, 'claudiom@gmail.com', 'claudioAudio'),
        Account(3, 'stinkylara@gmail.com', 'IStinkNice'),
        Account(4, 'newemail.com', 'NewUsername')
    ]
