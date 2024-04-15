"""
Write a function that accepts 2 args: an iterator/collection type and an element
Return the number of times the element appears in the iterator/collection
"""

def how_many(e, c):
    counter = 0
    for i in c:
        if i == e:
            counter += 1 # counter = counter + 1
    return counter

if __name__ == "__main__":
    x = how_many(1, ["1", 2, "1",1])
    print(x)