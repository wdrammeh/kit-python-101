def sum(x, y):
    print(x + y)

sum(10, 11)
sum(1100, 200)

def product(*args):
    print(args)
    print(type(args))
    for arg in args:
        print(arg)

product(3, 6)

def name(fname, lname):
    print(fname, lname)

name(lname='John', fname='Doe')