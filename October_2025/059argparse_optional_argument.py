import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-n","--name")
args = parser.parse_args()

if args.name:
	print(f"Hello, {args.name.title()}!")
else:
	print("Hello!")

