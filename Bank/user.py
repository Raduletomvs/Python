class User:
    def __init__(self, ssn, name):
        self.ssn = ssn
        self.name = name
        self.accounts = []

class InvalidUserData(Exception):
    def __init__(self):
        self.message = "Invalid user data provided."
