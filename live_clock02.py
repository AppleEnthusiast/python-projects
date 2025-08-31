from datetime import datetime
import time


print()
print("Live Clock (runs for 10 seconds)".center(70))
print()

start = time.time()

while time.time()-start < 10:
	now = datetime.now()
	print(now.strftime("\t%H:%M:%S"),end="\r")
	time.sleep(1)


print("\r\tGoodbye.")
