import argparse


parser = argparse.ArgumentParser(
	description="Displays the price for a product"
)
parser.add_argument("-n","--name",help="Product name")
parser.add_argument("-p","--price",type=float,help="Price for product")
args = parser.parse_args()

product = args.name
price = args.price

if product:
	if price is not None:
		print(f"{product}\t${price:.2f}")
	else:
		print(f"{product}\t-")
else:
	print("No product was entered.")

