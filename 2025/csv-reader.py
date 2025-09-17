try:
	with open("contacts.csv","r") as file:
		data = file.read().strip()

	contacts = data.split(";")

	for entry in contacts:
		name, phone = entry.split(",")
		print(f"Name: {name}\t| Phone: {phone}")

except FileNotFoundError:
	print("File was not found")
except Exception as e:
	print(f"Error: {e}")
