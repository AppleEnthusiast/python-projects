import argparse
from pathlib import Path


def get_filename() -> str:

	parser = argparse.ArgumentParser(
		description="Displays a text file"
	)

	parser.add_argument("-f","--file",help="Path to the input file")
	args = parser.parse_args()

	filename = (args.file or input("Enter filename: ")).strip()

	if not filename:
		parser.error("No filename provided")
	
	return filename


def read_file(filename: str) -> None:
	path = Path(filename)

	if not path.is_file():
		print(f"Error: '{filename}' was not found")
		return
	
	with path.open("r",encoding="utf-8") as fh:
		for index,line in enumerate(fh,start=1):
			print(f"{index:<10}{line}",end="")


def main() -> None:
	filename = get_filename()
	read_file(filename)


if __name__ == "__main__":
	main()

