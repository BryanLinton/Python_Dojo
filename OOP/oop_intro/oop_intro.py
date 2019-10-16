class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0
    def make_deposit (self, amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print("User: {}, Balance: {}".format(self.name, self.account_balance))
        

bubba = User("Bubba Gump", "bubbag@gmail.com")
guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
bubba.make_deposit(100).make_deposit(200).make_deposit(25).make_withdrawal(325)
guido.make_deposit(50).make_deposit(50).make_withdrawal(50).make_withdrawal(25)
monty.make_deposit(150).make_withdrawal(50).make_withdrawal(50).make_withdrawal(50)
bubba.display_user_balance()
guido.display_user_balance()
monty.display_user_balance()








