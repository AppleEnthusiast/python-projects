import sys


def main():
	if len(sys.argv) < 2:
		sys.exit("too few arguments")
	for arg in sys.argv[1:]:
		print("hello, i am",arg)

if __name__ == "__main__":
	main()
