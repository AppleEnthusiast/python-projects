cities = ["Rome","Hamburg","Berlin","Oslo","Amsterdam","Prague"]

print("Original:")
print(cities)
print()

cities.sort()
print("sort():")
print(cities)
print()

cities.sort(key=len)
print("sort(key=len)")
print(cities)

