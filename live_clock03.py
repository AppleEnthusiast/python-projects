from datetime import datetime
import time
import sys

print()
print("Live Clock".center(70))
print()

try:
	seconds = abs(int(input("\tHow long should the clock run (seconds)? ")))
except ValueError:
	sys.exit("Value Error")

start = time.monotonic()

try:
	while time.monotonic()-start < seconds:
		now = datetime.now()
		print(now.strftime("\t%H:%M:%S"),end="\r",flush=True)
		time.sleep(1)
except KeyboardInterrupt:
	print("\tProgram has been stopped by user")


print("\r\tHello. Goodbye.")
print()


