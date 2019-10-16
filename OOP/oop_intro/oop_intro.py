# class User:
#     def __init__(self, username, email_address):
#         self.name = username
#         self.email = email_address
#         self.account_balance = 0

#     def make_deposit(self, amount):
#         self.account_balance += amount
#         return self

#     def make_withdrawal(self, amount):
#         self.account_balance -= amount
#         return self

#     def display_user_balance(self):
#         print("User: {}, Balance: {}".format(self.name, self.account_balance))


class BankAccount:
    def __init__(self, int_rate, balance):
        self.rate = 0.03
        self.balance = 0.00

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print("Balance: {}".format(self.balance))

    def yield_interest(self):
        if self.balance > 0.00:
            self.balance = (self.rate * self.balance) + self.balance


bubba = (0.03, 0) 
bubba.deposit(100).deposit(200).deposit(25).withdrawal(325)
guido.make_deposit(50).make_deposit(50).make_withdrawal(50).make_withdrawal(25)

