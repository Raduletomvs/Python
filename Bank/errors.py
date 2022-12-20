class UserNotFound(Exception):
    def __init__(self):
        self.message = "User with the provided SSN was not found."

class InvalidMenuChoice(Exception):
    def __init__(self):
        self.message = "Invalid menu choice provided."

class InsufficientFunds(Exception):
    def __init__(self):
        self.message = "Insufficient"
