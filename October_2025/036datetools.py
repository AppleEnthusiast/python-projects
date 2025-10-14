from datetime import date

class DateTools:
	@staticmethod
	def is_weekend(d):
		return d.weekday() >= 5

	@staticmethod
	def days_diff(start,end):
		return (end - start).days


today = date.today()
vacation = date(2025,11,11)

if DateTools.is_weekend(today):
	print("It's weekend.")
else:
	print("Today is a workday.")

print("Days until vacation:",DateTools.days_diff(today,vacation),"days.")

