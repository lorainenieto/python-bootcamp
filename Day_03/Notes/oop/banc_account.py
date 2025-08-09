

class BankAccount:
    def __init__(self, initial_balance = 0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        self.balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        elif amount > self.balance:
            raise ValueError("Amount cannot be greater thatn balance")
        self.balance -= amount

    def print_balance(self):
        print(self.balance)











