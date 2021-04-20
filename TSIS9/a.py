import json
first = {"name": "Rakhman",
        "surname": "Magametov",
        "age": 21}

print(type(first))
second = json.dumps(first)
print(type(second))
third = json.loads(second)
print(type(third))