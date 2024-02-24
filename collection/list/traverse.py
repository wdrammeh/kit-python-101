fruits = ["apple", "banana", "orange", "melon", "mango"]

# value-based
for fruit in fruits:
    print(fruit)

# index-based
for i in range(len(fruits)):
    numb = i + 1
    print(numb, fruits[i])

# while
i = 0
while i < len(fruits):
    print(i, '=', fruits[i])
    i = i + 1
