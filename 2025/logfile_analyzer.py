print("Welcome to the Logfile Analyzer!")

# Ask the user for a filename
filename = input("Please enter the name of the logfile: ")

try:
    with open(filename, "r") as file:
        log = file.read()
except FileNotFoundError:
    print("The file was not found.")
    exit(1)

# Count how many times certain messages occur
error_count = log.count("ERROR")
warning_count = log.count("WARNING")
info_count = log.count("INFO")

total = error_count + warning_count + info_count

print("\nAnalysis results:")
print(f"ERROR messages: {error_count}")
print(f"WARNING messages: {warning_count}")
print(f"INFO messages: {info_count}")

# Percentage distribution (only if total > 0)
if total > 0:
    print("\nPercentage distribution:")
    print(f"ERROR:   {error_count / total * 100:.1f}%")
    print(f"WARNING: {warning_count / total * 100:.1f}%")
    print(f"INFO:    {info_count / total * 100:.1f}%")

# User can search for any custom term
search_term = input("\nWhich term should be searched in the log? ")
count = log.count(search_term)

print(f"The term '{search_term}' appears {count} times in the log.")

