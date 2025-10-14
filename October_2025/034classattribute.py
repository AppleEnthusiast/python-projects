class Book:
	total = 0

	def __init__(self,title):
		self.title = title
		Book.total += 1

	@classmethod
	def show_total(cls):
		print(f"total books: {cls.total}")


b1 = Book("1984")
b2 = Book("Der Tod in Venedig")

Book.show_total()

