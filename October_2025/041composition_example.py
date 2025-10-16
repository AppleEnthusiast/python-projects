class Engine:
	def start(self):
		print("Engine startet.")

class Car(Engine):
	def __init__(self):
		self.engine = Engine()

	def drive(self):
		self.engine.start()
		print("Car is driving.")


car = Car()
car.drive()

