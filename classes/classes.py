class Vehicle:
    def __init__(self, model, year) -> None:
        self.model = model
        self.year = year

    def moves(self):
        print("moves along..")


    def get_model(self):
        return self.model
    
    def set_model(self, model):
        self.model = model
        return self.model

my_car = Vehicle("Toyota", 2012)
print(my_car.model)
print(my_car.year)

my_car.moves()
print(my_car.get_model())
print(my_car.set_model("BMW"))
print(my_car.set_model("FORD"))

#inheritance

class Airplane(Vehicle):

    def __init__(self, model, year, size) -> None:
        super().__init__(model, year)
        self.size = size


    def fly():
        print("flying...")


air = Airplane("AirCraft", "2000", 4500)
print(air.model)
print(air.year)
print(air.size)
air.moves()