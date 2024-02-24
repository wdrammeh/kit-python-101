numbs = {2, 4, 6, 8, 10}
print(numbs)
print(type(numbs))
print(len(numbs))

# print(numbs[1]) # error: unordered

for numb in numbs:
    print(numb)

# numbs[5] = 12 # error: immutable

numbs.add(12)
print(numbs)

numbs.update([14, 16, 18, 20])
print(numbs)

# numbs.remove(x) # raises an error if no x
# numbs.discard() # no error on fail

removed_item = numbs.pop() # removes, returns random element
print('Removed', removed_item)