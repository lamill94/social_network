import pytest
from lib.database_connection import DatabaseConnection

# This is a pytest fixture i.e. a reusable funciton that provides setup logic for tests, supplying data or state before a test runs & cleaning up afterward
# It creates an object that we can use in our tests
# We will use it to create a DB connection

@pytest.fixture

def db_connection():
    connection = DatabaseConnection()
    connection.connect()
    return connection

# When a test includes a parameter named `db_connection`, Pytest automatically
# calls this fixture before the test runs and passes in its return value instead 
# of the function itself.

# We don’t need to call `db_connection()` or `db_connection.connect()` manually. For example:

# def test_something(db_connection):
#   db_connection's return value is now available to us in this test.