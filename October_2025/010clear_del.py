user_1 = {
	"name":"Anita",
	"age": 19,
	"city":"London"
}
user_2 = {
	"name":"Tim",
	"age": 21,
	"city":"Las Palmas / Gran Canaria"
}

print("Initial data of ",user_1.get("name",""),":",sep="")
print(user_1)
user_1.clear()
print("After clear():")
print(user_1)

print()

print("Initial data of ",user_2.get("name",""),":",sep="")
print(user_2)
del user_2

print()
print("Attempt to print after del:")
try:
	print(user_2)
except NameError as e:
	print(e)



