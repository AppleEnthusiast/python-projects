from datetime import datetime,timedelta

now = datetime.now()
today_2030 = now.replace(hour=20,minute=30,second=0,microsecond=0)
time_diff = today_2030 - now

if time_diff.total_seconds() < 0:
	today_2030 = today_2030 + timedelta(days=1)
	time_diff = today_2030 - now


time_diff = time_diff - timedelta(microseconds=time_diff.microseconds)
print(f"time now: {now.strftime('%H:%M')}")
print(f"time of appointment: {today_2030.strftime('%H:%M')}")
print(f"time left: {time_diff}")

