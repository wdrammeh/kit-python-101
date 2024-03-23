class Animal:
    
    def __init__(self, specie):
        self.specie = specie
        
    def run(self):
        print(f"{self.specie} is Running...")
        
    def eat(self):
        print(f"{self.specie} is Eating...")
        
    def sleep(self):
        print(f"{self.specie} is sleeping...")
        
    def make_sound(self):
        print("Blah blah")