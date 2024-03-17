class Rectangle:

    def __init__(self, width, length):
        self.width = width
        self.length = length

    def perimeter(self):
        perimeter = 2 * self.width + 2 * self.length
        return perimeter
    
    def area(self):
        area = self.width * self.length
        return area


if __name__ == "__main__":
    r1 = Rectangle(5, 10)

    print(r1.perimeter())
    print(r1.area())
