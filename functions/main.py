def say_hello():
    print('Hello')

# say_hello()

def say_hi(name):
    print('Hi', name)

say_hi('Muhammed')

def greet(persin1, person2):
    print('Greetings', persin1, 'and', person2)

greet('Ahmad', 'Sulayman')

# variable number of args
def welcome(*people):
    print('Welcome you all', people)

welcome('Alieu', 'Musa', 'Ibrahim', 'Fatou')

# args can be key-worded, in which case, position does not matter
greet(person2='Isabel', persin1='Maryam')

# arbitrary number of key-word args
def my_function(**person):
  print("His last name is " + person["lname"])

my_function(fname="Kawsu", lname="Jabi")

# default params
def nat(country='Gambia'):
    print('I am from', country)

nat()
nat('Mali')