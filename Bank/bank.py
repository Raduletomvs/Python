from account import InvalidAccountData, Account
from errors import UserNotFound, InvalidMenuChoice, InsufficientFunds
from user import User, InvalidUserData

class Bank:
    def __init__(self):
        self.users = []

    def create_user(self, ssn, name):
        user = User(ssn, name)
        self.users.append(user)

    def create_account(self, ssn, account_number):
        user = self.get_user(ssn)
        if user:
            account = Account(account_number)
            user.accounts.append(account)
        else:
            raise UserNotFound

    def get_user(self, ssn):
        for user in self.users:
            if user.ssn == ssn:
                return user
        return None

    def get_account(self, ssn, account_number):
        user = self.get_user(ssn)
        if user:
            for account in user.accounts:
                if account.account_number == account_number:
                    return account
            raise InvalidAccountData
        else:
            raise UserNotFound

    def deposit(self, ssn, account_number, amount):
        account = self.get_account(ssn, account_number)
        account.balance += amount

    def withdraw(self, ssn, account_number, amount):
        account = self.get_account(ssn, account_number)
        if account.balance >= amount:
            account.balance -= amount
        else:
            raise InsufficientFunds

    def print_users(self):
        for user in self.users:
            print(f"SSN: {user.ssn}, Name: {user.name}")

    def print_accounts(self, ssn):
        user = self.get_user(ssn)
        if user:
            for account in user.accounts:
                print(f"Account number: {account.account_number}, Balance: {account.balance}")
        else:
            raise UserNotFound

def main():
    bank = bank.Bank()

    while True:
        print("Menu:")
        print("1. Create user")
        print("2. Create account")
        print("3. Print all users")
        print("4. Print all accounts of a user")
        print("5. Deposit money into an account")
        print("6. Withdraw money from an account")
        print("7. Quit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                ssn = input("Enter SSN: ")
                name = input("Enter name: ")
                bank.create_user(ssn, name)
            elif choice == "2":
                ssn = input("Enter SSN: ")
                account_number = input("Enter account number: ")
                bank.create_account(ssn, account_number)
            elif choice == "3":
                bank.print_users()
            elif choice == "4":
                ssn = input("Enter SSN: ")
                bank.print_accounts(ssn)
            elif choice == "5":
                ssn = input("Enter SSN: ")
                account_number = input("Enter account number: ")
                amount = float(input("Enter amount: "))
                bank.deposit(ssn, account_number, amount)
            elif choice == "6":
                ssn = input("Enter SSN: ")
                account_number = input("Enter account number: ")
                amount = float(input("Enter amount: "))
                bank.withdraw(ssn, account_number, amount)
            elif choice == "7":
                break
            else:
                raise InvalidMenuChoice
        except InvalidUserData:
            print("Invalid user data provided.")
        except UserNotFound:
            print("User with the provided SSN was not found.")
        except InvalidAccountData:
            print("Invalid account data provided.")
        except InsufficientFunds:
            print("Insufficient funds in the account.")
        except InvalidMenuChoice:
            print("Invalid menu choice provided.")

if __name__ == "__main__":
    main()

