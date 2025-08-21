# Simple program: Show progress in percent

print("Welcome to the Progress Calculator!")
print("This program calculates your reading progress.")

# Ask for the total goal and the current progress
goal = int(input("How many pages do you want to read?")
progress = int(input("How many pages have you already read? "))

# Calculate share
share = progress / goal

# Output
print(f"You have read {progress} out of {goal}.")
print(f"That is {share:.1%} of your goal.")

