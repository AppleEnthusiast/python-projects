from datetime import date,timedelta

class Coupon:
	days_valid = 20

	def __init__(self,code):
		self.code = code
		self.valid_until = date.today() + timedelta(days=Coupon.days_valid)

	def is_valid(self):
		return date.today() <= self.valid_until

	def get_status(self):
		return "valid" if self.is_valid() else "expired"

	
my_coupon = Coupon("AppleEnthusiast123")
print("Coupon status:",my_coupon.get_status())

