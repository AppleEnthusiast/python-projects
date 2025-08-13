with open("secret_pwd.txt", "r") as file:
	pwd = file.read().strip()


code = input("Enter code: ")

if code == pwd:
	print("Code was correct.")
else:
	print("Permission denied")


