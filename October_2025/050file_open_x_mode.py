try:
	file = open("new_file.txt","x")
except FileExistsError:
	print("Error: The file already exists and can not be created again.")
else:
	file.write("The file was successfully created.\n")
	file.write("Python prevents overwriting existing files.\n")
	print("File successfully created and written.")
finally:
	try:	
		file.close()
		print("File was closed successfully.")
	except NameError:
		pass

