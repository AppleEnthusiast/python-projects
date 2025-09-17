import os

try:
    files_input = input("Enter file names (comma separated): ")
    files = [f.strip() for f in files_input.split(",")]

    print("\nFile sizes:")
    for file in files:
        if os.path.isfile(file):
            size = os.path.getsize(file)
            print(f"{file:<20} {size/1024:.2f} KB")
        else:
            print(f"{file:<20} File not found")

except Exception as e:
    print(f"An unexpected error occurred: {e}")

