def add_numbers(a,b):
	if isinstance(a,(int,float)) and isinstance(b,(int,float)):
		return a + b
	else:
		return "both values must be numbers"


print(add_numbers(57,68))
print(add_numbers(5.7,6.8))
print(add_numbers("nice try",68))
