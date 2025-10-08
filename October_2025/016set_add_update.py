numbers = {1,2,3}
print("Start:",numbers)
print()

numbers.add(4)
print("After add(4):")
print(numbers)
print()

numbers.update([5,6,7])
print("After update([5,6,7]):")
print(numbers)
print()

numbers.add(3)
numbers.update((6,8))

print("After add(3) and update((6,8))")
print(numbers)

