import time

class NegativeNumberError(Exception):
	pass

try:
	seconds = int(input("Enter seconds: "))
	if seconds < 0:
		raise NegativeNumberError("Please enter a positive number.")
except ValueError:
	print("Error: Please enter a number.")
except NegativeNumberError as e:
	print("Error:",e)
else:
	for i in range(seconds,0,-1):
		print(i)
		time.sleep(1)
	print("Countdown has ended.")
finally:
	print("End of program. Bye, bye!")

