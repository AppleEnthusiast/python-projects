# replace word in text file

def main():
	print()
	print("Word Replacer with Count".center(80))
	print()

	filename = input("Enter filename: ").strip()

	try:
		with open(filename,"r",encoding="utf-8") as f:
			text = f.read()

		old_word = input("Enter word you want to replace: ")
		new_word = input("Enter new word: ")

		count = text.count(old_word)

		if count == 0:
			print(f"'{old_word}' was not found in file.")
		else:
			new_text = text.replace(old_word,new_word)

			choice = input("overwrite original file? (y/n) ").lower()

			if choice == "y":
				file_to_save = filename
			else:
				file_to_save = f"modified_{filename}"

			with open(file_to_save,"w",encoding="utf-8") as f:
				f.write(new_text)

			print(f"'{old_word}' replaced by '{new_word}' {count} times.")
			print(f"File was saved as {file_to_save}")

	except FileNotFoundError:
		print("Error: file was not found.")
	except Exception as e:
		print(f"Unexpected error: {e}")


if __name__ == "__main__":
	main()
