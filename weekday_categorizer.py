def main():
    day = input("Enter a weekday (e.g. Monday): ").capitalize()
    categorize_day(day)

def categorize_day(day):
    match day:
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            print(f"{day} is a workday.")
        case "Saturday" | "Sunday":
            print(f"{day} is the weekend!")
        case _:
            print("Unknown day. Please enter a valid weekday.")

if __name__ == "__main__":
    main()

