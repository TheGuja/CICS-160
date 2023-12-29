from Car import Car

class GasolineCar(Car):
    def __init__(self, makeAndModel="none assigned", numberOfDoors = 4, maximumNumberOfPassengers = 5, gasTankSize = -1):
        super().__init__(makeAndModel, numberOfDoors, maximumNumberOfPassengers)
        self.gasTankSize = gasTankSize

    def getGasTankSize(self):
        return self.gasTankSize
    
    def setGasTankSize(self, int):
        self.gasTankSize = int

    def __str__(self):
        return f"{super().__str__()}\nGas Tank Size: {self.gasTankSize}"
    
