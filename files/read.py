
if __name__ == "__main__":
    file = open("test.txt", "r")
    content = file.read()
    print(content)

    # for line in file:
    #     print(line)

    file.close()
