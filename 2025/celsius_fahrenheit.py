def main():
	user_input = input("enter temperatures in celsius (separated by comma): ")
	try:

		temperatures = user_input.split(",")
		celsius = [float(t.strip()) for t in temperatures]
		fahrenheit = [round(c*9/5+32,1) for c in celsius]

		for c,f in zip(celsius,fahrenheit):
			print(f"{c}°C -> {f} F")

	except ValueError:
		print("error: incorrect input")
	except KeyboardInterrupt:
		print("program terminated by user")
	except Exception as e:
		print(f"unexpected error occured: {e}")



if __name__ == "__main__":
	main()
