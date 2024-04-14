"""
Write a function that accepts 2 args: a character and a string
Return the number of times the character appears in the string
"""

def how_many_times(char, string):
    counter = 0
    for s in string:
        if s == char:
            counter = counter + 1
    return counter

if __name__ == "__main__":
    x = how_many_times("m", "Jallow")
    print(x)