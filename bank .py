class BankAccount:
    def __init__(self, account_number, account_holder_name, account_balance):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = account_balance

    def deposit(self, amount):
        self.__account_balance += amount

    def withdraw(self, amount):
        if amount <= self.__account_balance:
            self.__account_balance -= amount
        else:
            print("Insufficient balance.")

    def display_balance(self):
        print("Account Balance:", self.__account_balance)


# Test the BankAccount class
account = BankAccount(123456789, "John Doe", 1000)
account.display_balance()  # Output: Account Balance: 1000

account.deposit(500)
account.display_balance()  # Output: Account Balance: 1500

account.withdraw(200)
account.display_balance()  # Output: Account Balance: 1300

account.withdraw(1500)  # Output: Insufficient balance.
account.display_balance()  # Output: Account Balance: 1300