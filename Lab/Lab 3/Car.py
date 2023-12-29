class Car:
    def __init__(self, make_model = "None assigned", num_doors = 4, max_passengers = 5):
        self.make_model = make_model
        self.num_doors = num_doors
        self.max_passengers = max_passengers

    def set_make_model(self, make_model):
        self.make_model = make_model

    def get_make_model(self):
        return (self.make_model)

    def set_num_doors(self, num_doors):
        self.num_doors = num_doors

    def get_num_doors(self):
        return (self.num_doors)

    def set_max_passengers(self, max_passengers):
        self.max_passengers = max_passengers

    def get_max_passengers(self):
        return (self.max_passengers)

    def __str__(self) -> str:
        return f"Make and Model:{self.make_model}\nNumber of doors: {self.num_doors}\nMaximum number of passengers: {self.max_passengers}"

if __name__ == "__main__":
    car1 = Car()
    car1.set_make_model("Dodge Dart")
    print(car1.get_make_model())
    print(car1)
