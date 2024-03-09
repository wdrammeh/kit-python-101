try:
    val = input("Enter age: ")
    age = int(val)
    this_year = 2024
    yob = this_year - age
    print(f"You are {age} years old")
    print(f"You were born in {yob}")
except:
    print("Error occurred")
else:
    print("No errors")
finally:
    print("AOB?")