from Car import Car
from Node import Node
from ElectricCar import ElectricCar
from GasolineCar import GasolineCar

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, e):
        newNode = Node(e)

        if self.size == 0:
            self.head = newNode
            self.tail = newNode
        else:
            current_last = self.tail
            current_last.setNext(newNode)
            newNode.setPrevious(current_last)
            self.tail = newNode

        self.size += 1

    def insert(self, index, object):
        newNode = Node(object)
        current = self.head

        if index == 0:
            current.setPrevious(newNode)
            newNode.setNext(current)
            self.head = newNode
        elif index == self.size - 1:
            newNode.setNext(self.tail)
            newNode.setPrevious(self.tail.getPrevious())
            self.tail.getPrevious().setNext(newNode)
            self.tail.setPrevious(newNode)
        elif index == self.size:
            current_last = self.tail
            current_last.setNext(newNode)
            newNode.setPrevious(current_last)
            self.tail = newNode
        else:
            for i in range(index):
                current = current.getNext()

            newNode.setNext(current)
            newNode.setPrevious(current.getPrevious())
            current.getPrevious().setNext(newNode)
            current.getNext().setPrevious(newNode)

        self.size += 1

    def length(self):
        return self.size     
    
    def __getitem__(self, index):
        current = self.head

        for i in range(index):
            current = current.getNext()

        return current.getData()

    def delete(self, index):
        if index >= self.size or index < 0:
            return
        
        if self.size == 1:
            self.head = None
            self.tail = None
        elif index == 0:
            self.head = self.head.getNext()
            self.head.setPrevious(None)
        elif index == self.size - 1:
            self.tail = self.tail.getPrevious()
            self.tail.setNext(None)
        else:
            current = self.head

            for index in range(index):
                current = current.getNext()

            current.getNext().setPrevious(current.getPrevious())
            current.getPrevious().setNext(current.getNext())

        self.size -= 1

    def __str__(self):
        current = self.head
        stringToReturn = str(current)

        while current.getNext() is not None:
            current = current.getNext()
            stringToReturn = stringToReturn + "\n\n" + str(current)
            

        return stringToReturn


if __name__ == "__main__":
    ll = LinkedList()
    car1 = Car("Toyota")
    car2 = ElectricCar("Tesla", batterySize = 4)
    car3 = GasolineCar("Lexus", gasTankSize = 5)
    car4 = Car("Guja")
    car5 = ElectricCar("Subu")

    # ll.add(car2)
    # ll.add(car3)
    # ll.insert(3, car4)
    ll.delete(0)

    # ll.add(1)
    # ll.add(2)
    # ll.add(3)
    # print(ll.head)

    
    # listToCompare = []
    # ll.delete(0)
    
    # current = ll.head
    # for i in range(ll.length()):
    #     listToCompare.append(current.getData())
    #     current = current.getNext()
    
