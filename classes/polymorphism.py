class Animal:
    
    def make_sound(self):
        print("making animal sound..")


class Dog(Animal):

    def make_sound(self):
        print("making DOG sound...")

class Fish(Animal):
    
    def make_sound(self):
        print("making fish sound..")



animal = Animal()
dog = Dog()
fish = Fish()

animal.make_sound()
dog.make_sound()
fish.make_sound()