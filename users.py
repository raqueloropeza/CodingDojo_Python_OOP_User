class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0

#instatiate new users
guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
rocky = User("Rocky Balboa", "rocky@python.com")

#make_deposit (self, amount) - have this method increase the user's balance by the amount specified
def make_deposit(self, amount):	
    self.account_balance += amount

#make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
def make_withdrawal(self, amount):
    self.account_balance -= amount

#display_user_balance(self) - have this method display the name and balance of the user specified.
def display_user_balance(self):
    print(f"User: {self.name}, Balance: {self.account_balance}")

#transfer_money -  have this method decrease the user's balance by the amount and add that amount to other other_user's balance
def transfer_money(self, other_user, amount):
    self.account_balance -= amount
    self = other_user
    self.account_balance += amount

make_deposit(guido,200)
make_deposit(guido, 50)
make_deposit(guido, 100)
make_withdrawal(guido, 1)
display_user_balance(guido)
make_deposit(monty,10)
make_deposit(monty,100)
make_withdrawal(monty,1)
make_withdrawal(monty,4)
display_user_balance(monty)
make_deposit(rocky,500)
make_withdrawal(rocky,20)
make_withdrawal(rocky,25)
make_withdrawal(rocky,5)
display_user_balance(rocky)
transfer_money(guido,rocky,100)
display_user_balance(guido)
display_user_balance(rocky)
