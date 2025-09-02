import random
random.seed()

print("Simple Calculator")
print("Choose an operation: +, -, *, /")

operation = input("Operation: ")
a = random.randint(1, 10)
b = random.randint(1, 10)

match operation:
    case "+":
        print(f"Result: {a} + {b} = {a + b}")
    case "-":
        print(f"Result: {a} - {b} = {a - b}")
    case "*":
        print(f"Result: {a} * {b} = {a * b}")
    case "/":
        if b != 0:
            print(f"Result: {a} / {b} = {a / b}")
        else:
            print("Error: Division by zero not allowed.")
    case _:
        print("Unknown operation.")

