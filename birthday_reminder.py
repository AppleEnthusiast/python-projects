from datetime import date

print("Welcome to my Birthday Reminder".center(70))
print()

today = date.today()
print(f"Today is {today.day}.{today.month}.{today.year}\n")

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
    birthday_this_year = date(today.year, month, day)
except ValueError:
    print("That date does not exist. Please check day and month (e.g., 31.04 is invalid).")
    raise SystemExit(1)

print(f"\n{name} has a birthday on {day}.{month}.")

# Determine the next birthday (this year or next year)
if birthday_this_year < today:
    next_birthday = date(today.year + 1, month, day)
else:
    next_birthday = birthday_this_year

days_left = (next_birthday - today).days

# Output
if days_left == 0:
    print(f"Today is the day: {name} has a birthday! 🎉")
elif days_left == 1:
    print("The birthday is tomorrow.")
else:
    if next_birthday.year == today.year:
        print(f"The birthday is still ahead — in {days_left} days.")
    else:
        print(f"The next birthday of {name} is in {days_left} days.")

