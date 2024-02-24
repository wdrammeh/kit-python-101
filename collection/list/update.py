fruits = ["banana", "cherry", "kiwi", "melon"]
print(fruits)

fruits.append('orange')
print(fruits)

fruits.insert(0, 'apple')
print(fruits)

countries = ['Gambia', 'Senegal', 'Spain']
countries.extend(fruits)
print(countries)

fruits[0] = 'Apple'
fruits[1:3] = ["blackcurrant", "watermelon"]
print(fruits)