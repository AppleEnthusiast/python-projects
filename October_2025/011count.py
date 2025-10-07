cart = ["Apple","Banana","Orange","Apple","Apple","Bread"]
print("Current shopping cart:")
print(cart)

product = input ("Which product do you want to count? ").title()
count = cart.count(product)

if count > 0:
	print(f"{product} appears {count} time(s) in your cart.")
else:
	print(f"'{product}' was not found in your shopping cart.")

