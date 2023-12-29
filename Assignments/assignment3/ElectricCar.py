from Car import Car

class ElectricCar(Car):
    def __init__(self, makeAndModel="none assigned", numberOfDoors = 4, maximumNumberOfPassengers = 5, batterySize = -1):
        super().__init__(makeAndModel, numberOfDoors, maximumNumberOfPassengers)
        self.batterySize = batterySize

    def getBatterySize(self):
        return self.batterySize
    
    def setBatterySize(self, int):
        self.batterySize = int

    def __str__(self):
        return f"{super().__str__()}\nBattery Size: {self.batterySize}"