from fractions import Fraction

x = Fraction(3, 7)
y = Fraction(8, 9)

print(x)
print(type(x))
print(f"Numerator: {x.numerator}")
print(f"Denominator: {x.denominator}")

print()
print(f"{x} + {y} = {x + y}")
print(f"{x} - {y} = {x - y}")
print(f"{x} / {y} = {x / y}")
print(f"{x} * {y} = {x * y}")

y = Fraction(1, 3)
print(f"{x} ** {y} = {x ** y:.4f}")

