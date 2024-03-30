class Operation:

    def __init__(self, x, y, opr):
        self.x = x
        self.y = y
        self.operator = opr
    
    def operate(self):
        if self.operator == "+":
            return self.x + self.y
        elif self.operator == "-":
            return self.x - self.y
        elif self.operator == "*":
            return self.x * self.y
        elif self.operator == "/":
            return self.x / self.y
        elif self.operator == "mod":
            return self.x % self.y
        else:
            return None
