import json

# loads for loading a string
x =  '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
print(type(y))
print(y)
print(y["age"])

# load for loading a file stream
with open("person.json", "rt") as f:
    person = json.load(f)
    print(person)
