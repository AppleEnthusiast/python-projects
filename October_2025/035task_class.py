from datetime import date,timedelta

class Task:
	def __init__(self,title,days_until_due):
		self.title = title
		self.created_on = date.today()
		self.due_date = self.created_on + timedelta(days=days_until_due)

	def remaining_days(self):
		rest = (self.due_date - date.today()).days
		return max(rest,0)

	def show(self):
		print(self.title)
		print(f"Due on {self.due_date} ({self.remaining_days()} days remaining)")


t1 = Task("Finish Project",5)
t2 = Task("System Reboot",10)

t1.show()
print()
t2.show()

