def method_1():
    val = input("Enter age: ")
    age = int(val)
    this_year = 2024
    yob = this_year - age
    print(f"You are {age} years old")
    print(f"You were born in {yob}")


def method_2():
    try:
        val = input("Enter age: ")
        age = int(val)
        this_year = 2024
        yob = this_year - age
        print(f"You are {age} years old")
        print(f"You were born in {yob}")
    except: # only when error occur
        print("Error occurred")
    else: # only when no errors occur
        print("No errors occurred")
    finally: # always executes
        print("End of block")


if __name__ == "__main__":
    method_1()
    # method_2()