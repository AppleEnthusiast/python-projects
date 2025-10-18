file = open("text.txt","a")
text = """
	This text was sent from my Python program.
		Enjoy learning Python!
"""
file.write(text)
file.close()
print("Text was written into file.")

