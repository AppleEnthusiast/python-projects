class Message:
	def __init__(self,text):
		self.text = text
	
	def send(self):
		print("Message:",self.text)


class Email(Message):
	def __init__(self,text,recipient):
		super().__init__(text)
		self.recipient = recipient

	def send(self):
		print(f"E-Mail to {self.recipient}: {self.text}")


class SMS(Message):
	def __init__(self,text,number):
		super().__init__(text)
		self.number = number

	def send(self):
		print(f"SMS to {self.number}: {self.text}")



email = Email("Hey, how are you?","me@somewhere.com")
sms = SMS("on my way","1234 - 567891234")

email.send()
sms.send()

