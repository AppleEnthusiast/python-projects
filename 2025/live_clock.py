from datetime import datetime
import time

print()
print("Live Clock (press ctrl+C to stop)".center(70))
print()

try:
	while True:
		now = datetime.now()
		print(now.strftime("\t%H:%M:%S"),end="\r")
		time.sleep(1)
except KeyboardInterrupt:
	print("\r\tProgram stopped by user.")

print("\tEnd of program. Goodbye.")
