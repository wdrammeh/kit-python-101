# import random
from random import randint, choice

if __name__ == "__main__":
    lower_bound = 1
    upper_bound = 10

    log = open("mathquiz.txt", "at")

    correct = 0
    total = 0

    while True:
        num1 = randint(lower_bound, upper_bound)
        num2 = randint(lower_bound, upper_bound)

        operators = ["+", "-", "*", "/", "mod"]

        opr = choice(operators)

        answer = input(f"{num1} {opr} {num2} = ")
        if answer == "q":
            break

        try:
            answer = float(answer)
        except:
            print("Invalid input.")
            continue

        if opr == "+":
            result = num1 + num2
        elif opr == "-":
            result = num1 - num2
        elif opr == "*":
            result = num1 * num2
        elif opr == "/":
            result = num1 / num2
        elif opr == "mod":
            result = num1 % num2
        
        if answer == result:
            print(True)
            correct = correct + 1
        else:
            print(False, f"[ {result} ]")

        total = total + 1

        log.write(f"{num1} {opr} {num2} = {result}\n")

    log.close()
    print(f"\nTotal score: {correct}/{total} ({round((correct/total)*100)}%)")