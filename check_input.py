def get_int():
	while True:
		try:
			return int(input("> ").strip())
		except ValueError:
			print("please enter an integer value")
		except KeyboardInterrupt:
			print("\nprogram terminated by user")
			raise SystemExit


print(f"your number: {get_int()}")
print("hello goodbye")

