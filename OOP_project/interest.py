from bank_account import *

class InterestRewardAccount(BankAccount):

    def __init__(self, balance, account_name) -> None:
        super().__init__(balance, account_name)

    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("Deposit with interest complete")
        return self.balance