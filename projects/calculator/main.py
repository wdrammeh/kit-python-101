from models import Operation

if __name__ == "__main__":
    print("Welcome to my calculator app")

    log = open("log.txt", "at")

    while True:
        # Read the user input
        expr = input("> ")
        # Get rid of unnecessary spaces
        expr = expr.replace(" ", "")

        if expr == "q":
            break

        x = y = opr = None
        
        if expr.__contains__("+"):
            opr = "+"
        elif expr.__contains__("-"):
            opr = "-"
        elif expr.__contains__("*"):
            opr = "*"
        elif expr.__contains__("/"):
            opr = "/"
        elif expr.__contains__("mod"):
            opr = "mod"

        try:
            vars = expr.split(opr)
            x = int(vars[0])
            y = int(vars[1])
        except:
            print("Error")
            continue

        operation = Operation(x, y, opr)
        answer = operation.operate()
        print(answer)
        log.write(f"{x} {opr} {y} = {answer} \n")
        
    log.close()
    print("Goodbye")