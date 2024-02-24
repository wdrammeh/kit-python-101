person = {
   'name': 'Muhammed Drammeh',
   'age': 25,
   'address': 'Sukuta',
   'is_married': False
}

print(person)
print(type(person))
print(len(person))

print(person['name'])

# print(person['country']) # error
print(person.get('country'))

person['country'] = 'Gambia'
print(person)

for x in person:
    print(x)

for key in person.keys():
    print(key, '=', person[key])

for val in person.values():
    print(val)

for x, y in person.items():
    print(x, y)