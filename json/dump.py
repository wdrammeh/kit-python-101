import json

person = {
  "name": "John Daw",
  "age": 30,
  "city": "New York"
}

print(type(person))
print(person)

# dump for dumping a file stream
with open("person.json", "wt") as f:
    json.dump(person, f, indent=4)

# dumps for dumping a string
person = json.dumps(person)
print(type(person))
print(person)