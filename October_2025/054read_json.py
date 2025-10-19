import json

try:
	with open("data.json","r") as fh:
		data = json.load(fh)
except FileNotFoundError:
	print("Error: File was not found.")
else:
	for key,value in data.items():
		if isinstance(value,list):
			value = ", ".join(value)
		print(f"{key.title()}: {value}")
finally:
	print("End of program. Bye, bye!")

