# Am adding 3 numbers
def sum_1(x, y, z):
    sum = x + y + z
    print(sum)

# Give me any count of numbers
# I'll print their sum
def sum_2(*nums):
    sum = 0
    for num in nums:
        sum = sum + num
    print(sum)

sum_2(3, 6, 9, 12)