import math
import random


def get_rand_numb():
    x = random.randint(1, 10)
    return x


if __name__ == "__main__":
    print(math.ceil(1.2))
    print(math.floor(6.9))
    print(math.sqrt(9))
    print(math.pi)

    print(get_rand_numb())