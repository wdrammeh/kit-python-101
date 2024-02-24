fruits = ["banana", "cherry", "kiwi", "melon"]
print(fruits)

fruits.remove('kiwi') # removes the 1st occurence of the arg

fruits.pop() # removes last

fruits.pop(1)

print(fruits)
# del fruits[0]
# print(fruits)

# del fruits # removes memory ref
fruits.clear()
print(fruits)