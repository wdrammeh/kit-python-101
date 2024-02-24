fruits = ["banana", "mango", "orange", "melon"]
print(fruits)

fruits.remove('orange') # removes the 1st occurence of the arg
print(fruits)

fruits.pop() # removes last
print(fruits)

fruits.pop(1)
print(fruits)
# del fruits[0]
# print(fruits)

# del fruits # removes memory ref
fruits.clear()
print(fruits)