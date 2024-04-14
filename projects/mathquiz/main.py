import random

if __name__ == "__main__":
    lower_bound = 1
    upper_bound = 10

    operators = ["+", "-", "*", "/", "mod"]

    x = random.randint(lower_bound, upper_bound)
    y = random.randint(lower_bound, upper_bound)

    opr = random.choice(operators)

    result = None

    if opr == "+":
        result = x + y
    elif opr == "-":
        result = x - y
    elif opr == "*":
        result = x * y
    elif opr == "/":
        result = x / y
    elif opr == "mod":
        result = x % y

    print(f"> {x} {opr} {y}")
    answer = input("")
    answer = int(answer)

    if answer == result:
        print(True)
    else:
        print(False)