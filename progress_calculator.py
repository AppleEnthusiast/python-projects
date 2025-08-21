# Simple program: Show progress in percent

print("Welcome to the Progress Calculator!")

# Ask for the total goal and the current progress
goal = int(input("What is your goal? (e.g. number of pages, euros, kilometers): "))
progress = int(input("How much have you already achieved? "))

# Calculate share
share = progress / goal

# Output
print(f"You have completed {progress} out of {goal}.")
print(f"That is {share:.1%} of your goal.")

