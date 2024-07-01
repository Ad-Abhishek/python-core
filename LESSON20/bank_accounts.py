class BalanceException(Exception):
    pass


class BankAccount():
    def __init__(self, accountName, initialBalance):
        self.name = accountName
        self.balance = initialBalance
        print(f"Account '{self.name}' created \n Balance: {self.balance}")

    def get_balance(self):
        print(f"'{self.name}' balance: {self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print("Deposited successfully ✅")
        self.get_balance()

    def viable_transaction(self, amount):
        if (self.balance >= amount):
            return
        else:
            raise BalanceException(
                f"Sorry, account '{self.name}' only has ${self.balance:.2f}")

    def withdraw(self, amount):
        try:
            self.viable_transaction(amount)
            self.balance = self.balance - amount
            print("\n Withdraw complete.")
            self.get_balance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")

    def transfer(self, amount, account):
        try:
            self.viable_transaction(amount)
            self.balance = self.balance - amount
            self.get_balance()
            account.deposit(amount)
            print("\nTransaction complete✅\n\n**********")
        except BalanceException as error:
            print(f"Transfer interrupted.❌ {error}")


class InterestRewarsAccount(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\n Deposit complete.")
        self.get_balance()


class SavingAccount(InterestRewarsAccount):
    def __init__(self, accountName, initialBalance):
        super().__init__(accountName, initialBalance)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viable_transaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\n Withdraw complete.")
            self.get_balance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")
