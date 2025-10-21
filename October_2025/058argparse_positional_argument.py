import argparse


parser = argparse.ArgumentParser()
parser.add_argument("word")
args = parser.parse_args()
print(f"Word that has been entered as argument: '{args.word}'")

