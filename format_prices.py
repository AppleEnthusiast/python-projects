price = 49.99
quantity = 30

total = price * quantity

print(f"us-format: ${total:,.2f}")
print(f"de-format: {total:,.2f} €".replace(",","X").replace(".",",").replace("X","."))

