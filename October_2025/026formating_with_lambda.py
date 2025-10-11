prices = [4.5,1234.56,29,109.9]
currency_formatted = lambda p: f"${p:,.2f}"

for price in prices:
	print(currency_formatted(price))

