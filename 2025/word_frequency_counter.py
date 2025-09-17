print()
print("word frequency counter".title().center(80))
print()

try:
	with open(input("\tenter filename: "),"r",encoding="utf-8") as file:
		text = file.read()

	words = text.split()
	word_count = {}

	for word in words:
		word = word.strip(",;:.-_!?()<>[]{}\"§$%&/*")
		if word:
			word_count[word] = word_count.get(word,0) + 1

	words_sorted = sorted(word_count.items(),key=lambda x:x[1],reverse=True)

	print()
	for word,count in words_sorted[:12]:
		print(f"\t{word:<15}{count:>15}")
	print()
except FileNotFoundError:
	print("file was not found")
except Exception as e:
	print(f"unexpected error occured: {e}")
