class NegativeNumberError(Exception):
	pass

def calculate_square_root(number:float) -> float:
	if number < 0:
		raise NegativeNumberError("Negative number - no real square root possible")
	return number**0.5

def main():
	try:
		value = float(input("Enter a number: "))
		result = calculate_square_root(value)
	except ValueError:
		print("Please enter a number.")
	except NegativeNumberError as e:
		print("Error:",e)
	else:
		print(f"Result: {round(result,2)}")


if __name__ == "__main__":
	main()

