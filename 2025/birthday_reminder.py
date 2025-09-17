from datetime import date

print()
print("Welcome to my Birthday Reminder".center(70))
print()

today = date.today()
# Display date in German style 
print(f"Today is {today.day:02d}.{today.month:02d}.{today.year}\n")

# User input
name = input("Whose birthday should I remember? ").title()
try:
    day = int(input("Enter the birthday (day) (1-31): "))
    month = int(input("Enter the birthday (month) (1-12): "))
except ValueError:
    print("Please enter valid numbers for day and month.")
    raise SystemExit(1)

# Try to build the birthday date for this year (catch invalid dates like 31.04)
try:
    birthday = date(today.year, month, day)
except ValueError:
    print("That date does not exist.")
    raise SystemExit(1)

# Determine the next birthday (this year or next year)
if birthday < today:
    birthday = date(today.year + 1, month, day)

days_left = (birthday - today).days

print(f"\n{name} has a birthday on {birthday.day:02d}.{birthday.month:02d}.{birthday.year}")

# Output
if days_left == 0:
    print(f"Today is the day: {name} has a birthday! 🎉")
elif days_left == 1:
    print("The birthday is tomorrow.")
else:
    print(f"The birthday is still ahead — in {days_left} days.")

