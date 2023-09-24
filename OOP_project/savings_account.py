from interest import *

class SavingAccount(InterestRewardAccount):
    def __init__(self, balance, account_name) -> None:
        super().__init__(balance, account_name) 
        self.fee = 5

    def withdraw_from_savings(self, amount):
        try:
            self.withdraw_money(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            return self.balance
        except BalanceException as error:
            print(f"{BalanceException} => withdraw interrupted")