# Simple unit converter using match-case (Python 3.10+)

print()
print("Unit Converter".center(50, "-"))
print()

print("\tChoose an option:")
print("\t-----------------------------")
print("\t1 - Kilometers to Miles")
print("\t2 - Miles to Kilometers")
print("\t3 - Inches to Centimeters")
print("\t4 - Centimeters to Inches")
print("\t5 - Feet to Meters")
print("\t6 - Meters to Feet")

print()
choice = input("\tYour choice: ")
print()

try:
    match choice:
        case "1":
            km = float(input("\tEnter distance in kilometers: "))
            miles = km * 0.621371
            print(f"\t{km} km = {miles:.2f} miles")
        case "2":
            miles = float(input("\tEnter distance in miles: "))
            km = miles / 0.621371
            print(f"\t{miles} miles = {km:.2f} km")
        case "3":
            inch = float(input("\tEnter length in inches: "))
            cm = inch * 2.54
            print(f"\t{inch} in = {cm:.2f} cm")
        case "4":
            cm = float(input("\tEnter length in centimeters: "))
            inch = cm / 2.54
            print(f"\t{cm} cm = {inch:.2f} in")
        case "5":
            foot = float(input("\tEnter length in feet: "))
            meter = foot * 0.3048
            print(f"\t{foot} ft = {meter:.2f} m")
        case "6":
            meter = float(input("\tEnter length in meters: "))
            foot = meter / 0.3048
            print(f"\t{meter} m = {foot:.2f} ft")
        case _:
            print("\tInvalid choice.")

except Exception as e:
    print(f"\tError message: {e}")
    raise SystemExit("\tHello Goodbye")

print()
print("\tHello Goodbye")
print()
