class Animal:

    def __init__(self, kind:str, color:str) -> None:
        self.kind = kind
        self.color = color

    
    def make_animal_sound(self):
        print("making animal sound")


class Creature:

    def creature(self):
        print("creature")



class Dog2(Animal, Creature):

    def __init__(self, kind: str, color: str) -> None:
        super().__init__(kind, color)



dog = Dog2("Pug", "Beige")
dog.creature()