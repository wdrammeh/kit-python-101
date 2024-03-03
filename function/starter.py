def greet():
    print('Hello, world!')


def percent(numb, x):
    result = x/100 * numb
    return result


def get_avg(numbs):
    sum = 0
    for numb in numbs:
        sum += numb
    f = len(numbs)
    avg = sum / f
    return avg


def get_min(numbs):
    min = numbs[0]
    for numb in numbs:
        if numb < min:
            min = numb
    return min


def get_max(numbs):
    pass


if __name__ == '__main__':
    # print('The average is', get_avg([1, 2, 3, 4]))
    print('The min is', get_min([10, 2, 3, 4]))