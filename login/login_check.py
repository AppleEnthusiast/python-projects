try:
	with open("secret_pwd.txt", "r") as file:
		pwd = file.read().strip()

except FileNotFoundError:
	print("Error: File Not Found")
	exit(1)


code = input("Enter code: ")

if code == pwd:
	print("Code was correct.")
else:
	print("Permission denied")


