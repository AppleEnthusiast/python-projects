numbers = [9,1,5,2]

a = numbers.copy()
b = numbers.copy()
c = numbers.copy()

print("original list:")
print(numbers)
print()

a.reverse()
print("reverse():")
print(a)
print()

b.sort()
print("sort():")
print(b)
print()

c.sort(reverse=True)
print("sort(reverse=True):")
print(c)
print()

