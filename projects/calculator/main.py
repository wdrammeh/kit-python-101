print("Welcome to my calculator app")
while True:
    # Read the user input
    expr = input("> ")
    # User wants to quit?
    if expr == "q":
        break
    # Get rid of unnecessary spaces
    expr = expr.replace(" ", "")
    # Addition?
    if expr.__contains__("+"):
        # Split the input string to get the two numbers
        vars = expr.split("+")
        try:
            x = int(vars[0])
            y = int(vars[1])
            result = x + y
            print(result)
        except:
            print("Error")
    # Subtraction?
    elif expr.__contains__("-"):
        vars = expr.split("-")
        try:
            x = int(vars[0])
            y = int(vars[1])
            result = x - y
            print(result)
        except:
            print("Error")
    # Modulus
    elif expr.__contains__("mod"):
        vars = expr.split("mod")
        try:
            x = int(vars[0])
            y = int(vars[1])
            result = x % y
            print(result)
        except:
            print("Error")
    else:
        print("Error")

print("Goodbye!")