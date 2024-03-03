# This is a function that accepts any number of int agruments
# And returns their sum
def sum(*numbs):
    sum = 0
    for numb in numbs:
        sum = sum + numb # sum += numb
    return sum


print(sum(1, 2, 3, 4))