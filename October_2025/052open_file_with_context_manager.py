try:
	with open("dummy_text","r") as file:
		content = file.read()
except FileNotFoundError:
	print("Error: File was not found.")
else:
	print(content)
finally:
	print("End of program.")

