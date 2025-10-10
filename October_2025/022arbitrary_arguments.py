def list_items(*items):
	if not items:
		print("No items were passed.")
		return

	for i,e in enumerate(items,start=1):
		print(f"{i:>2}. {e.upper()}")


list_items()
print()

list_items("Apple","Banana","Cherry")
print()

list_items("Cake","Pie")
print()

list_items("Waffles")

