print("Welcome to my calculator app")
while True:
    # Read the user input
    expr = input("> ")
    if expr == "q":
        break
    # Get rid of unnecessary spaces
    expr = expr.replace(" ", "")
    # Additio?
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
    elif expr.__contains__("-"):
        # Split the input string to get the two numbers
        vars = expr.split("-")
        try:
            x = int(vars[0])
            y = int(vars[1])
            result = x - y
            print(result)
        except:
            print("Error")
    elif expr.__contains__("mod"):
        # Split the input string to get the two numbers
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