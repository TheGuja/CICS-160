# Author: Eric Gu
# Email: ejgu@umass.edu
# Spire ID: 34231523
# Synchronizer / Liason: Eric
# Reflector: Archie

class Car:
    def __init__(self, make_model = "None assigned", num_doors = 4, max_passengers = 5):
        self.make_model = make_model
        self.num_doors = num_doors
        self.max_passengers = max_passengers
    
    def set_make_model(self, model):
        self.make_model = model

    def set_num_doors(self, doors):
        self.num_doors = doors

    def set_max_passengers(self, passengers):
        self.max_passengers = passengers

    def get_make_model(self):
        return self.make_model
    
    def get_num_doors(self):
        return self.num_doors

    def get_max_passengers(self):
        return self.max_passengers
    
    def __str__(self):
        stringToReturn = (f"Make and Model: {self.make_model}\nNumber of doors: {str(self.num_doors)}\nMaximum number of passengers: {str(self.max_passengers)}")
        return stringToReturn



if __name__ == "__main__":
    car1 = Car()
    car1.set_make_model("Dodge Dart")
    car1.set_num_doors(5)
    car1.set_max_passengers(7)

    print(car1.get_make_model())
    print(car1.get_num_doors())
    print(car1.get_max_passengers())
    print(car1)

    car2 = Car()
    print(car2)

    car3 = Car("BMW", 5, 7)
    print(car3)