print("Welcome to your Phonebook")

contacts = {
	"Anna": "0151- 1234567",
	"Ben": "0170-7654321",
	"Clara": "0160-9876543"
}

print("-" * 60)
# print(contacts.items())

print("Type 'list' to see all contacts or 'exit' to quit.")

while True:
	name = input("\nWhose number do you want to see? ")

	if name == "exit":
		print("Program terminated. Goodbye.")
		break
	elif name == "list":
		for person, number in contacts.items():
			print(f"{person}: {number}")
	elif name in contacts:
		print(f"{name}: {contacts[name]}")
	else:
		print(f"{name} is not in the phonebook.")


print("-" * 60)


