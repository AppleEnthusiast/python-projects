# Simple program to demonstrate text alignment with f-strings

items = [
    ("Apple", 0.99),
    ("Banana", 0.59),
    ("Milk", 1.49),
    ("Bread", 2.49),
    ("Cheese", 4.75)
]

print("WELCOME TO PYTHON SHOP".center(30, "-"))  # centered title
print()

# Print header
print(f"{'Item':<15}{'Price':>15}")
print("-" * 30)

# Print items
for name, price in items:
    print(f"{name:<15}{price:>15.2f}")

print("-" * 30)
total = sum(price for _, price in items)
print(f"{'Total':<15}{total:>15.2f}")

