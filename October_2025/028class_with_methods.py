class Lamp:
	def __init__(self,color):
		self.color = color
		self.is_on = False

	def turn_on(self):
		self.is_on = True
		print("The lamp has been turned on.")

	def turn_off(self):
		self.is_on = False
		print("The lamp has been turned off.")

	def check(self):
		if self.is_on:
			print("The lamp is on")
		else:
			print("The lamp is off")


my_lamp = Lamp("yellow")
print("Color of lamp is:",my_lamp.color)

my_lamp.turn_on()
my_lamp.check()

my_lamp.turn_off()
my_lamp.check()


		
