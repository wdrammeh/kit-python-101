names = ['Muhammed', 'Ibrahim', 'Yusuf', 'Amie', 'Fatou']
print(names)

names.append('Kaddy')
print(names)

names.extend(['John', 'Mustapha', 'Kathrine'])
print(names)

names.remove('Amie')
print(names)

for name in names:
    print(name)

i = 0
while i < len(names):
    print(names[i])
    i = i + 1