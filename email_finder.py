import sys

print("Welcome to the Email Finder!\n")
filename = input("Please enter filename: ")

# open and read the file
try:
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
except FileNotFoundError:
    sys.exit("File was not found.")

# look for '@'
pos = content.find("@")

if pos != -1:
    # find word boundaries around the '@'
    start = content.rfind(" ", 0, pos) + 1    # begin right after the previous space (or 0)
    end = content.find(" ", pos)              # stop at next space
    if end == -1:
        end = len(content)

    # slice and strip common punctuation stuck to the address
    email = content[start:end].strip(".,;:!?()[]{}<>\"'")
    print(f"Found email address: {email}")
else:
    print("No email address found in the file.")

