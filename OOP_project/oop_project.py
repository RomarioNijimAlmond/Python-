from bank_account import *
from interest import *
from savings_account import *

account1 = BankAccount(1000, "Dave")
account2 = BankAccount(2000, "John")

print(account1.get_balance())
print(account2.get_balance())


account1.set_balance(3000)
print(account1.get_balance())

account2.deposit(2000)
print(account2.get_balance())


account2.withdraw(2000)
print(account2.get_balance())

account2.withdraw(1000)
print(account2.get_balance())

# account2.withdraw(2000)
# print(account2.get_balance())

account2.withdraw_money(500)
print(account2.get_balance())

# account2.withdraw_money(1000)
# print(account2.get_balance())

# account1.transfer_money(1000, account2)

# print(account1.get_balance())
# print(account2.get_balance())

# account1.transfer_money(100000, account2)

account3 = InterestRewardAccount(2000, "Jim")
account3.deposit(1000)
print(account3.get_balance())

account4 = SavingAccount(5000,"Sara")
# account4.withdraw_money(2000)
# print(account4.get_balance())
account4.withdraw_from_savings(2000)
print(account4.get_balance())