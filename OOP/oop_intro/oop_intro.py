class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account = BankAccount ()

class BankAccount:
    def __init__(self, initial_balance = 0):
        self.int_rate = 0.03
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print("Balance: {}".format(self.balance))
        return self

    def yield_interest(self):
        if self.balance > 0.00:
            self.balance = (self.int_rate * self.balance) + self.balance
        else:
            print("No balance to apply interest")
        return self


bubba = User("Bubba", "bubbag@gmail.com") 
guido = User("Guido", "guido@gmail.com")
bubba.account.deposit(100).deposit(100).deposit(50).withdraw(150).yield_interest().display_account_info()
guido.account.deposit(50).deposit(50).withdraw(50).withdraw(25).yield_interest().display_account_info()

