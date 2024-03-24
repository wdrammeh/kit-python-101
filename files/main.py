import os

# x - create a new file - error if file exists
# a - append contents to an existing file - create file if it does not exist
# w - write - overwrite file if exists otherwise create a new file

# r - read - opens a file for reading

if __name__ == "__main__":
    # Create
    # file = open("test.txt", "w")
    # file.write("Welcome to The Gamnia")
    # file.close()

    # Read
    # file = open("gambia.txt", "r")
    # content = file.read()
    # print(content)
    # file.close()

    if os.path.exists("test.txt"):
        print("File exists")
        os.remove("test.txt")
        print("Removed.")
    else:
        print("File does not exist")
    # os.remove("test.txt")