def remove_vowels(text):
	vowels = "aeiouAEIOU"
	table = str.maketrans("","",vowels)
	return text.translate(table)


def main():
	sentence = "Python Programming is Amazing"
	print("Original:",sentence)
	print("Without vowels:",remove_vowels(sentence))


if __name__ == "__main__":
	main()

