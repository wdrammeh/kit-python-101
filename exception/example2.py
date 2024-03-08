# Exception handled

if __name__ == "__main__":
    val = input("Enter year of birth: ")
    try:
        yob = int(val)
        print("You were born", yob)
    except:
        print("Error!")

    this_year = 2024
    age = this_year - yob
    print("You are", age, "years old")
