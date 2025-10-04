def main():
	try:
		country = input("enter country (de|at|ch): ").upper()
		price = float(input("enter price: "))
		calc_vat(country,price)
	except ValueError:
		print("Invalid input. Please enter a number.")

def calc_vat(country,price):
	match country:
		case "DE" | "GERMANY":
			print(f"Germany (19% VAT): {price*1.19:.2f} EUR")
		case "AT" | "AUSTRIA":
			print(f"Austria (20%): {price*1.2:.2f} EUR")
		case "CH" | "Switzerland":
			print(f"Switzerland (7.7% VAT): {price*1.077:.2f} CHF")
		case _:
			print("unknown country")

if __name__ == "__main__":
	main()
