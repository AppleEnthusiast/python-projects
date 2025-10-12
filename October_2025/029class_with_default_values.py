class Account:
	def __init__(self,owner,balance=0):
		self.owner = owner
		self.balance = balance

	def display_balance(self):
		print(f"Account balance for {self.owner}: ${self.balance:.2f}")


account_1 = Account("Anna")
account_2 = Account("Charlie",500)

account_1.display_balance()
account_2.display_balance()

