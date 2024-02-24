langs = ('Python', 'Java', 'C++', 'C#')
print(langs)
print(type(langs))
print(len(langs))

for lang in langs:
    print(lang)

for i in range(len(langs)):
    print(i, langs[i])

i = 0
while i < len(langs):
    print(i, langs[i])
    i = i + 1
