import sys


def main():
	if len(sys.argv) < 2:
		sys.exit("Too few arguments")
	elif len(sys.argv) > 2:
		sys.exit("Too many arguments")

	print(f"Hello, {sys.argv[1].title()}!")


if __name__ == "__main__":
	main()


