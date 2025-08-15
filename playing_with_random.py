import random as r

print("Playing with random numbers.")

for _ in range(10):
	num = r.randint(1,6)
	print(f"{num} ", end=" ")


print()
print(f"End of program")
