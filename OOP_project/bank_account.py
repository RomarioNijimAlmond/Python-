class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, balance, account_name) -> None:
        self.balance = balance
        self.account_name = account_name
        print(f"\nAccount '{self.account_name}' created.\nBalance = ${self.balance:.2f}")

    def get_balance(self):
        return self.balance

    def set_balance(self, balance):
        self.balance = balance
        return self.balance
    
    def deposit(self, deposit_amount):
        self.balance = self.balance + deposit_amount
        return self.balance
    
    def withdraw(self,withdraw_amount):
        if self.balance >= withdraw_amount:
            self.balance = self.balance - withdraw_amount
            return self.balance
        else:
            raise BalanceException("the current balance is less than the withdraw amount")
        
    def withdraw_money(self, amount):
        try:
            self.withdraw(amount)
        except:
            raise BalanceException("the amount that your trying to withddraw is bigger than the actual balance")
        
    def transfer_money(self, amount, account):
        try:
            print("********** Beginning transfer")
            self.withdraw(amount)
            account.deposit(amount)
        except BalanceException as error:
            print(f"{error}: transfer was interrupted")