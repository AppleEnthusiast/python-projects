cart = ["rice","pasta","salt","sausage","honey","tea","coffee","ice cream"]
print("original list:")
print(cart)
print()

cart.sort(key=lambda product:(len(product),product))
print("length - alphabetical")
print(cart)
print()

cart.sort(key=lambda product:(product,len(product)))
print("alphabetical - length:")
print(cart)
print()

