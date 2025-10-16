class BankAccount:
	def __init__(self,balance):
		self.__balance = balance

	def deposit(self,amount):
		if amount > 0:
			self.__balance += amount
			print(f"Deposited ${amount}. New balance: ${self.__balance}.")
		else:
			print("Invalid amount.")

	def withdraw(self,amount):
		if amount <= self.__balance:
			self.__balance -= amount
			print(f"Withdrew ${amount}. New balance: ${self.__balance}.")
		else:
			print("Insufficient funds!")
			
	def get_balance(self):
		return self.__balance


account = BankAccount(100)
account.deposit(50)
account.withdraw(30)
print(f"Balance: {account.get_balance()}")

