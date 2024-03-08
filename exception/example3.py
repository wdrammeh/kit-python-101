# Functions extracted

def get_yob():
    val = input("Enter year of birth: ")
    try:
        yob = int(val)
        return yob
    except:
        print("Error")
        return None


def get_age(yob):
    this_year = 2024
    age = this_year - yob
    return age


if __name__ == "__main__":
    yob = get_yob()
    age = get_age(yob)
    print("You were born", yob)
    print("You are", age, "years old")