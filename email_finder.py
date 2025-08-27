print("Welcome to the Email Finder!\n")

# open and read the file
with open("text.txt", "r", encoding="utf-8":) as file:
    content = file.read()

# look for '@'
pos = content.find("@")

if pos != -1:
    # find word boundaries
    start = content.rfind(" ", 0, pos) + 1
    end = content.find(" ", pos)
    if end == -1:
        end = len(content)

    email = content[start:end]
    print(f"Found email address: {email}")
else:
    print("No email address found in the file.")

