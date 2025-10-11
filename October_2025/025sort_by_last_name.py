names = ["John Lennon","Paul McCartney","George Harrison","Ringo Star"]
print("Original list:")
print(names)
names.sort(key=lambda n: n.split()[1])
print("After sort():")
print(names)

