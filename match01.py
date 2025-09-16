def main():
	name = input("What's your name? ").title()
	hello()
	hello(name)

def hello(to="world"):
	match to:
		case "Teoman" | "Teo" | "Teoman Dogueri":
			print("Hello, my friend. Nice to see you again.")
		case "Sarman":
			print("hello, my dear cat. I remember you well.\nrest peacefully in "
					"God's arms.")
		case _:
			print(f"hello, {to}")


if __name__ == "__main__":

	main()
