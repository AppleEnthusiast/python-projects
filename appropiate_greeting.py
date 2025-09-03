from datetime import datetime


now = datetime.now()

match now.hour:
	case h if h < 12:
		print("Good Morning")
	case h if h < 18:
		print("Good Afternoon")
	case _:
		print("Good Evening")


