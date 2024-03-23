from animal import Animal


class Dog(Animal):

    def __init__(self):
        super().__init__("Dog")

    
    def make_sound(self):
        print("Waw waw!")