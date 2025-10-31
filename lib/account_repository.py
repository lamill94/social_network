from lib.account import Account

class AccountRepository:

    # Initialise with database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all accounts
    def all(self):
        rows = self._connection.execute_query('SELECT * from accounts')
        accounts = []
        for row in rows:
            item = Account(row["id"], row["email"], row["username"])
            accounts.append(item)
        return accounts
    
    # Create a new account
    def create(self, account):
        rows = self._connection.execute_query('INSERT INTO accounts (email, username) VALUES (%s, %s) RETURNING id', [account.email, account.username])
        row = rows[0]
        return row["id"]