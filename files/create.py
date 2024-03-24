"""
x - Create - will try cresting new file - error if exists
w - Write - will overwrite any existing content - create if not existed
"""

if __name__ == "__main__":
    f = open("test.txt", "w")
    f.write("Welcome to the Gambia")
    f.close()
