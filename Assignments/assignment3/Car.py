class Car:
    def __init__(self, makeAndModel = "none assigned", numberOfDoors = 4, maximumNumberOfPassengers = 5):
        self.makeAndModel = makeAndModel
        self.numberOfDoors = numberOfDoors
        self.maximumNumberOfPassengers = maximumNumberOfPassengers

    def setMakeAndModel(self, string):
        self.makeAndModel = string

    def getMakeAndModel(self):
        return self.makeAndModel
    
    def getMaximumNumberOfPasengers(self):
        return self.maximumNumberOfPassengers
    
    def __str__(self):
        return f"Car: {self.makeAndModel}\nNumber of Doors: {self.numberOfDoors}\nNumber of Passengers: {self.maximumNumberOfPassengers}"