"""
Write a function that accepts a list arg
Return its reverse
"""

def reverse(col):
    i = len(col) - 1
    rev = []
    while i >= 0:
        rev.append(col[i])
        i = i - 1
    return rev

if __name__ == "__main__":
    list = [1, 2, 3, 4, 5, 6, 7]
    list_reverse = reverse(list)
    print(list)
    print(list_reverse)
