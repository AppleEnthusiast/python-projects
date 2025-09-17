from datetime import datetime
import time
import threading

print()
print("\t🕒 Live Clock (press ENTER to stop)".center(60))
print()

# Flag for terminating programm
stop = False

def wait_for_input():
    global stop
    input()
    stop = True

threading.Thread(target=wait_for_input).start()

while not stop:
    now = datetime.now()
    print(now.strftime("\t%H:%M:%S"), end="\r",flush=True)
    time.sleep(1)

print()
print("\tClock stopped")
print("\tHello Goodbye")
print()
