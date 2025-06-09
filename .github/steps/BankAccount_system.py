class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        print(f"Depositing {amount} to {self.holder}'s account.")
        new_balance = amount + self.balance
        self.balance = new_balance
        print(f"New balance is {self.balance}.")

    def withdraw(self, amount):
        if amount <= self.balance:
            new_balance = self.balance - amount
            self.balance = new_balance
            print(f"Withdrawing {amount} from {self.holder}'s account.")
        else:
            print(f"Insufficient funds for {self.holder} account to withdraw {amount}. Current balance is {self.balance}")

    def check_balance(self):
        print(f"{self.holder}'s current balance is {self.balance}.")

AliceAccount = BankAccount("Alice", 1000)
AliceAccount.deposit(500)
AliceAccount.withdraw(200)
AliceAccount.withdraw(1500)
AliceAccount.check_balance()