class Shape:
	def area(self):
		pass

class Circle(Shape):
	def __init__(self,radius):
		self.radius = radius

	def area(self):
		print("Calculating circle area...")
		return 3.14 * self.radius**2

class Rectangle(Shape):
	def __init__(self,width,height):
		self.width = width
		self.height = height
		
	def area(self):
		print("Calculating rectangle area...")
		return self.width * self.height


shapes = [Circle(3),Rectangle(4,5)]

for shape in shapes:
	print()
	result = shape.area()
	print("Area:",result)
	print()

