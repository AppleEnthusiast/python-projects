from datetime import datetime


def daytime_greeting():
	now = datetime.now()
	match now.hour:
		case h if h < 12:
			print("good morning")
		case h if h < 18:
			print("good afternoon")
		case _:
			print("good evening")


def main():
	daytime_greeting()


if __name__ == "__main__":
	main()

