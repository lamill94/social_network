class Account:

    # Constructor method
    def __init__(self, id, email, username):
        self.id = id
        self.email = email
        self.username = username

    # This method allows our tests to assert that the objects it expects are the objects we made based on the database records
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # This method makes it look nicer when we print an account
    def __repr__(self):
        return f"Account({self.id}, {self.email}, {self.username})"