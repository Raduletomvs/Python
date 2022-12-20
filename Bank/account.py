class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

class InvalidAccountData(Exception):
    def __init__(self):
        self.message = "Invalid account data provided."
