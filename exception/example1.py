# Exception not handled

if __name__ == "__main__":
    val = input("Enter year of birth: ")
    yob = int(val)
    print('You were born', yob)
    this_year = 2024
    age = this_year - yob
    print("You are", age, "years old")