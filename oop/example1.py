class Rectangle:
    pass


if __name__ == "__main__":
    r1 = Rectangle()
    print(type(r1))
    r1.width = 5
    r1.length = 10
    r1.perimeter = 2 * r1.width + 2 * r1.length
    r1.area = r1.width * r1.length

    r2 = Rectangle()
    r2.width = 10
    r2.length = 15
    r2.perimeter = 2 * r2.width + 2 * r2.length
    r2.area = r1.width * r2.length

    print(r1.perimeter)
    print(r2.area)