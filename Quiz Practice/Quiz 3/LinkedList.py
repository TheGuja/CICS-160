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
    
    def length(self):
        return self.size
    
    def bubble_once(self):
        if self.length() == 0:
            return

        current = self.head

        while (current.getNext() is not None):
            if (current.getData() > current.getNext().getData()):
                temp = current.getData()
                current.setData(current.getNext().getData())
                current.getNext().setData(temp)

            current = current.getNext()

    def bubble_all(self):
        for i in range(self.length()):
            self.bubble_once()

    def putBiggestAtEnd(self, upToHere):
        if upToHere > 0:
            indexOfBiggest = 0
            current = self.head

            for i in range(upToHere + 1):
                if current.getData() > self[indexOfBiggest]:
                    indexOfBiggest = i
                
                current = current.getNext()
                

            temp = self[upToHere]
            self[upToHere] = self[indexOfBiggest]
            self[indexOfBiggest] = temp

    def selection_sort(self):
        biggestIndexToLookAt = self.length() - 1

        while biggestIndexToLookAt != 0:
            # print(f"hi {biggestIndexToLookAt}")
            self.putBiggestAtEnd(biggestIndexToLookAt)
            # print(self)
            biggestIndexToLookAt -= 1

        return self
    
    def mergeSort(self):
        if self.length() < 2:
            return self
        else:
            a = LinkedList()
            b = LinkedList()

            a_sorted = LinkedList()
            b_sorted = LinkedList()

            for i in range(self.length() // 2):
                a.add(self[i])

            for i in range(self.length() // 2, self.length()):
                b.add(self[i])

            a_sorted = a.mergeSort()
            b_sorted = b.mergeSort()

            return self.merge(a_sorted, b_sorted)

    def merge(self, a, b):
        newList = LinkedList()

        a_current = a.head
        b_current = b.head

        while ((a_current is not None) and (b_current is not None)):
            if a_current.getData() < b_current.getData():
                newList.add(a_current.getData())
                a_current = a_current.getNext()
            else:
                newList.add(b_current.getData())
                b_current = b_current.getNext()

        while a_current is not None:
            newList.add(a_current.getData())
            a_current = a_current.getNext()

        while b_current is not None:
            newList.add(b_current.getData())
            b_current = b_current.getNext()

        return newList

        # a_index = 0
        # b_index = 0

        # while (a_index < a.length() and b_index < b.length()):
        #     if (a[a_index] < b[b_index]):
        #         newList.add(a[a_index])
        #         a_index += 1
        #     else:
        #         newList.add(b[b_index])
        #         b_index += 1

        # while a_index < a.length():
        #     newList.add(a[a_index])
        #     a_index += 1

        # while b_index < b.length():
        #     newList.add(b[b_index])
        #     b_index += 1

        # return newList

    def __getitem__(self, index):
        current = self.head

        for i in range(index):
            current = current.getNext()

        return current.getData()
    
    def __setitem__(self, index, o):
        current = self.head

        for i in range(index):
            current = current.getNext()

        current.setData(o)

    def __str__(self):
        current = self.head
        stringToReturn = str(current)

        while current.getNext() is not None:
            current = current.getNext()
            stringToReturn = stringToReturn + "\n" + str(current)
            

        return stringToReturn
    
if __name__ == "__main__":
    ll = LinkedList()
    ll.add(7)
    ll.add(6)
    ll.add(5)
    ll.add(4)
    ll.add(3)
    ll.add(2)

    a_ll = LinkedList()
    a_ll.add(5)
    a_ll.add(6)
    a_ll.add(7)

    b_ll = LinkedList()
    b_ll.add(1)
    b_ll.add(2)
    b_ll.add(3)
    
    new = ll.mergeSort()
    print(new)