tasks = input("enter tasks (seperated by comma): ").strip().split(",")
status = dict.fromkeys(tasks,"not done")

print("tasks:")
print(status)

