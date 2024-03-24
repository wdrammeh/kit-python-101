from animal import Animal
from donkey import Donkey
from dog import Dog

if __name__ == "__main__":
    animal = Animal("Unknown")
    animal.run()
    
    dog = Dog()
    # print(dog.specie)
    dog.run()
    # dog.make_sound()
    
    donkey = Donkey()
    # print(donkey.specie)
    donkey.run()
    
    # donkey.make_sound()