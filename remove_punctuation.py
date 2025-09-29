import string

def remove_punctuation(text):
	return text.translate(str.maketrans("","",string.punctuation))


def main():
	sentence = "Hello, World! Python is an amazing programming language! :-))"
	print(sentence)
	print(remove_punctuation(sentence))


if __name__ == "__main__":
	main()

