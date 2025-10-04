import statistics

def main():
	# grades according to the German school system
	grades = [1.3,2.0,2.7,3.3,1.7,4.0,5.0,2.7,3.7,6.0]

	print()
	print("Grade Statistics")
	print("Grades",grades)
	print("Mean",round(statistics.mean(grades),2))
	print("Median",round(statistics.median(grades),2))
	print("Standard Devation:",round(statistics.stdev(grades),2))


if __name__ == "__main__":
	main()
