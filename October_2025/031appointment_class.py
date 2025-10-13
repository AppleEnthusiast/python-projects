from datetime import datetime,date,time

class Appointment:

	def __init__(self,title,year,month,day,hour,minute):
		self.title = title
		try:
			self.time_point = datetime.combine(date(year,month,day),time(hour,minute))
		except ValueError as e:
			print("Error:",e)
			self.time_point = None

	def show(self):
		if self.time_point:
			print(f"{self.title:<30}- {self.time_point.strftime('%d.%m.%Y, %H:%M')}")
		else:
			print(f"{self.title:<30}")

		
appointments = [
	Appointment("Collect Lottery Winnings",2026,1,2,9,15),
	Appointment("Flight to the Caribbean",2026,1,3,14,0),
	Appointment("Singing and Dancing Event",2025,12,31,19,30)
]

appointments.sort(key=lambda a: a.time_point or datetime.max)

for appointment in appointments:
	appointment.show()

