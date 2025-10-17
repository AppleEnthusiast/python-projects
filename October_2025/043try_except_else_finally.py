try:
	number = int(input("Enter a number: "))
	result = 10/number
except ValueError as e:
	print("Error:",e)
except ZeroDivisionError as e:
	print("Error:",e)
else:
	print("Result:",round(result,2))
finally:
	print("End of programm. Bye, bye and see you later!")

