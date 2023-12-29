from Person import Person
from Node import Node

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

    def delete(self, i):

        if i >= self.size or i < 0:
            return False
        
        if self.size == 1:
            self.head = None
            self.tail = None
        elif i == 0:
            self.head = self.head.getNext()
            self.head.setPrevious(None)
        elif i == self.size - 1:
            self.tail = self.tail.getPrevious()
            self.tail.setNext(None)
        else:
            current = self.head

            for index in range(i):
                current = current.getNext()

            current.getNext().setPrevious(current.getPrevious())
            current.getPrevious().setNext(current.getNext())

        self.size -= 1
        return True
    
    def insert_after(self, after_this_val, val):
        current = self.head
        insertion = False

        while current is not None:

            if current.getData() == after_this_val:
                newNode = Node(val)
                newNode.setNext(current.getNext())
                newNode.setPrevious(current)

                if current.getNext() is not None:
                    current.getNext().setPrevious(newNode)
                else:
                    self.tail = newNode

                current.setNext(newNode)
                insertion = True
                current = newNode.getNext()

            else:
                current = current.getNext()

        return insertion
    
    def count(self, target):

        current = self.head
        number_nodes = 0

        while current is not None:
            if current.getData() == target:
                number_nodes += 1
            current = current.getNext()

        return number_nodes
    
    # def swap(self, i, j):
    #     current_i = self.head
    #     current_j = self.head
    #     swap = False

    #     for index in range(i):
    #         current_i = current_i.getNext()
    #         i_previous = current_i.getPrevious()
    #         i_next = current_i.getNext()

    #     for index in range(j):
    #         current_j = current_j.getNext()
    #         j_previous = current_j.getPrevious()
    #         j_next = current_j.getNext()

    #     current_i.setNext(j_next)
    #     current_i.setPrevious(j_previous)
    #     j_previous.setNext(current_i)
    #     j_next.setPrevious(current_i)
        

    #     current_j.setNext(i_next)
    #     current_j.setPrevious(i_previous)
    #     i_previous.setNext(current_j)
    #     i_next.setPrevious(current_j)

        
    #     return swap


    def __str__(self):
        stringToReturn = "List size: " + str(self.size)
        current = self.head
        while (current is not None):
            stringToReturn = stringToReturn + "\n\n" + str(current)
            current = current.getNext()
        return(stringToReturn)

if __name__ == "__main__":
    ll = LinkedList()

    person1 = Person("Harry", '123-456-7890')
    person2 = Person("James", '987-654-3210')
    person3 = Person("Potter", '555-444-3333')
    person4 = Person("Ron", '555-444-333')

    ll.add(person1)
    ll.add(person2)
    ll.add(person3)
    ll.insert_after(person1, person4)
    ll.swap(2, 3)
    print(ll)