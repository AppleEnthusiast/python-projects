from datetime import datetime
import time

print()
print("Live Clock (press ctrl+C to stop)".center(70))
print()

while True:
	now = datetime.now()
	print(now.strftime("\t%H:%M:%S"),end="\r")
	time.sleep(1)

print("End of program. Goodbye.")
