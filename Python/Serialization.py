import pickle
import json

def serialize():
	testDict = {
	"things" : ["apple", "orange", "pen", "table"],
	"year" : 2002,
	"name" : "Ryan"
	}

	with open("pickleFile", "wb") as file:
		pickle.dump(testDict, file)


def deserialize():
	with open("pickleFile", "rb") as file:
		content = pickle.load(file)
		print(json.dumps(content, indent=4, sort_keys=True))

serialize()
deserialize()
input()
