from random import randint


print()
print("dice simulator".title().center(80))
print()

try:
	rolls = int(input("\thow many times should the dice be rolled? "))

	dice = [randint(1,6) for _ in range(rolls)]
	count = {}
	
	for number in dice:
		count[number] = count.get(number,0)+1
	
	print()
	for n,f in sorted(count.items()):
		print(f"\t{n:<10}{f:>10}")
	print()
except ValueError:
	print("value error")
except Exception as e:
	print("unexpected error occured: {e}")
