# this is my first file on the repository

def hello_world():
	msg = f"""
		Hello, world!
		I'm happy starting over with Python.
	"""
	print(msg)


def hello_user(name):
	print(f"Hello, {name}! Nice to meet you.")


hello_world()

name = input("What's your name? ")

hello_user(name)
