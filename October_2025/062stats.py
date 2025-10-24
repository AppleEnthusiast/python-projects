import argparse
from pathlib import Path


def main():
	parser = argparse.ArgumentParser(
		description="Displays statistics of a text file"
	)

	parser.add_argument("-f","--file",required=True,help="Path to the input file")

	args = parser.parse_args()
	filename = args.file

	path = Path(filename)
	
	if not path.is_file():
		parser.error(f"Error: could not find '{filename}'")
	
	lines = words = chars = 0

	with path.open("r",encoding="utf-8",errors="replace") as fh:
		for line in fh:
			lines += 1
			words += len(line.split())
			chars += len(line.rstrip("\n"))

	print(f"Lines:      {lines:>12}")
	print(f"Words:      {words:>12}")
	print(f"Characters: {chars:>12}")


if __name__ == "__main__":
	main()

