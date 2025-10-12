class Product:
	def __init__(self,name,price):
		self.name = name
		self.price = price

products = [
	Product("Bread",2.5),
	Product("Milk",1.2),
	Product("Cheese",3.4)
]

for p in products:
	print(f"{p.name}:\t${p.price}")

