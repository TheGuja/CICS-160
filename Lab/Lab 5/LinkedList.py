import Person

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, e):
        if self.size == 0:
            self.head = e
            self.tail = e
        else:
            current_last = self.tail
            current_last.setNext(e)
            e.setPrevious(current_last)
            self.tail = e
        self.size = self.size + 1

    def delete(self, i):

        current_element = self.head
        
        for index in range(i + 1):
            current_element = current_element
            after = current_element.getNext()
            before = current_element.getPrevious()
            current_element = current_element.getNext()
            
        self.size -= 1

        if before is None:
            if after is None:
                self.head = None
                self.tail = None
                return
            
            after.setPrevious(None)
            self.head = after
            return
        
        if after is None:
            before.setNext(None)
            self.tail = before
            return

        after.setPrevious(before)
        before.setNext(after)

    def __str__(self):
        stringToReturn = "List size: " + str(self.size)
        current = self.head
        while (current is not None):
            stringToReturn = stringToReturn + "\n\n" + str(current)
            current = current.getNext()
        return(stringToReturn)

if __name__ == "__main__":
    listOfPeople = LinkedList()
    listOfPeople.add(Person.Person("Jaime", "Amherst"))
    listOfPeople.add(Person.Person("Maria", "Stow"))
    listOfPeople.add(Person.Person("Maria", "Malden"))

    listOfPeople.delete(0)
    #listOfPeople.delete(0)
    #listOfPeople.delete(0)

    # listOfPeople.delete(2)
    # listOfPeople.delete(1)
    # listOfPeople.delete(0)
    print(listOfPeople)
