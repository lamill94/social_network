from lib.database_connection import DatabaseConnection
from lib.account_repository import AccountRepository
from lib.post_repository import PostRepository

# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/social_network.sql")

# Instantiate an Account object
account_repository = AccountRepository(connection)

# Retrieve & list out all Accounts
accounts = account_repository.all()

for account in accounts:
    print(account)

# Instantiate a Post object
post_repository = PostRepository(connection)

# Retrieve & list out all Posts
posts = post_repository.all()

for post in posts:
    print(post)