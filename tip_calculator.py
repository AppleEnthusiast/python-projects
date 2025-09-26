import sys

def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python tip.py <amount> <tip-percent>")

    try:
        amount = float(sys.argv[1])
        tip_percent = float(sys.argv[2])
    except ValueError:
        sys.exit("Please enter numbers only.")

    tip = amount * (tip_percent / 100)
    total = amount + tip

    print(f"Bill: {amount:.2f} €")
    print(f"Tip ({tip_percent}%): {tip:.2f} €")
    print(f"Total: {total:.2f} €")

if __name__ == "__main__":
    main()

