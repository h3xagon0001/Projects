import json

# python dict
pythonDict = {
    "name": "John",
    "age": 28,
    "married": False,
    "email": ("johnsmith@mail.com", "johnbuisness@officemail.com"),
    "pets": None,
    "watch": {
        "brand": "Fossil", "price": 199.9
    }
}

jsonObject = json.dumps(pythonDict, indent=4)

print(jsonObject)