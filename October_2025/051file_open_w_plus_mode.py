file = open("new_file","w+")
file.write("old text in file was deleted\n")
file.write("greeting from python file.\n")
file.seek(0)
print(file.read())
file.close()

