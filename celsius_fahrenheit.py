try:
	user_input = input("Enter temperatures in Celsius (seperated by comma): ")
	
	temperatures = user_input.split(",")
	celsius = [float(temp.strip()) for temp in temperatures]
	print(celsius)
	
	fahrenheit = [round(temp *9/5+32,1) for temp in celsius]
	print(fahrenheit)
	
	for c, f in zip(celsius,fahrenheit):
		print(f"{c} °C -> {f} F")
except ValueError:
	print("Incorrect Input")
except Exception as e:
	print(f"{e}")
