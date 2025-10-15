class Document:
	def __init__(self,title):
		self.title = title

	def save(self):
		print(f"Saving document: {self.title}")


class PDF(Document):
	def save(self):
		super().save()
		print(f"Exporting {self.title} as PDF file")


class Pages(Document):
	def save(self):
		super().save()
		print(f"Saving {self.title} as Pages document")


docs = [PDF("Report"),Pages("Letter")]

for d in docs:
	d.save()

