try:
	names_input = input("enter participant names (separated by comma): ")
	times_input = input("enter times in seconds (separated by comma): ")

	names = [name.strip() for name in names_input.split(",")]
	times_sec = [int(value.strip()) for value in times_input.split(",")]

	times_min_sec = [(t//60,t%60) for t in times_sec]

	print()
	print("-"*50)
	for name, sec, (m,s) in zip(names,times_sec,times_min_sec):
		print(f"{name:<12}{sec:>4} sec --> {m}:{s:02d} min")
	print("-"*50)
except ValueError:
	print("invalid input")
except Exception as e:
	print(f"unexpected error: {e}")
