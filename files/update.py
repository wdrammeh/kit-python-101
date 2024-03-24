"""
a - Append - will append to the end of a file - create, if does not exist
"""

if __name__ == "__main__":
    f = open("test.txt", "a")
    f.write("The smiling coast of Africa")
    f.close()
