john = dict(name = "John", age = 36, country = "Norway")
print(john)
print(type(john))
print(len(john))

if 'wife' in john:
    print('Wife is present')
else:
    print('No wife present')

john.update({'wife': 'Katherine'})
print(john)

john.pop('age')
# del john['age']
print(john)
# john.clear()