class WeakPasswordError(Exception):
	def __init__(self,password,message="password is too weak"):
		super().__init__(f"{message}: {password}")


def check_password(password):
	if len(password) < 6:
		raise WeakPasswordError(password)
	print("password accepted")

def main():
	try:
		pw = input("enter password: ")
		check_password(pw)
	except WeakPasswordError as e:
		print(e)
	else:
		print("registration was successful")
	finally:
		print("end of programm. bye bye")

if __name__ == "__main__":
	main()

