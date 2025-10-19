import json

data = {
	"name":"Teoman",
	"age":57,
	"city":"Future City",
	"hobbies": ["Python","Meditation","Exercice","Reading"]
}

with open("data.json","w") as fh:
	json.dump(data,fh,indent=4)

print("JSON file was created")

