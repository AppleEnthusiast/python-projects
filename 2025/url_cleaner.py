print("Welcome to the URL Cleaner (File Version)")

# Open the file and read all lines
with open("urls.txt", "r") as file:
    urls = file.readlines()

print("\nCleaning URLs...\n")

for url in urls:
    # Remove leading/trailing whitespace like \n
    url = url.strip()

    # Clean https:// or http:// prefix
    clean_url = url.removeprefix("https://").removeprefix("http://")

    print(f"Original: {url}")
    print(f"Cleaned : {clean_url}\n")

