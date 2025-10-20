from datetime import datetime

note = input("Enter your note: ")
time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("notes.txt","a") as fh:
	fh.write(f"[{time_stamp}] {note}\n")

print("Note was saved.")

