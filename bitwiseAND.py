print()
def get_age():
	while True:
		try:
			return int(input("enter your age: ").strip())
		except ValueError:
			print("please enter your age")
		except KeyboardInterrupt:
			print("program terminated by user")
			raise SystemExit

age = get_age()
check = 0b00000001
print()
print(f"\t{age:08b}\t({age})")
print(f"&\t{check:08b}\t({check})")
print("-------------------------------")
print(f"\t{age & check:08b}")

print("\t\b", "odd" if age & check else "even")
