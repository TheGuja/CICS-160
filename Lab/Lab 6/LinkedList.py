# Synchronizer: Eric
# Liason: Hayun
# Reflector: Jenny

from Node import Node
import unittest
  
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
    self.size = self.size + 1

  def bubble_once(self):

    if self.size == 0:
      return 
    
    current = self.head

    while (current.getNext() is not None):

      if current.getData() > current.getNext().getData():
        temp = current.getData()
        current.setData(current.getNext().getData())
        current.getNext().setData(temp)

      current = current.getNext()

  def bubble(self):
    for i in range(self.size):
      self.bubble_once()

  def __str__(self):
    stringToReturn = "List size: " + str(self.size)
    current = self.head

    while (current is not None):
      stringToReturn = stringToReturn + "\n\n" + str(current)
      current = current.getNext()

    return(stringToReturn)
  
class Test_BubbleSort(unittest.TestCase):
  def setUp(self):
      self.ll_test = LinkedList()

  def test_emptyList_once(self):
    self.ll_test.bubble_once()

    listToCompare = []
    current = self.ll_test.head
    while current is not None:
      listToCompare.append(current.getData())
      current = current.getNext()

    self.assertEqual(listToCompare, [])
     
  def test_emptyList_all(self):
    self.ll_test.bubble()

    listToCompare = []
    current = self.ll_test.head
    while current is not None:
        listToCompare.append(current.getData())
        current = current.getNext()

    self.assertEqual(listToCompare, [])

  def test_alreadySorted_once(self):
    self.ll_test.add(1)
    self.ll_test.add(2)
    self.ll_test.add(3)
    self.ll_test.add(4)

    self.ll_test.bubble_once()

    listToCompare = []
    current = self.ll_test.head
    while current is not None:
        listToCompare.append(current.getData())
        current = current.getNext()

    self.assertEqual(listToCompare, [1, 2, 3, 4])

  def test_alreadySorted_all(self):
    self.ll_test.add(1)
    self.ll_test.add(2)
    self.ll_test.add(3)
    self.ll_test.add(4)

    self.ll_test.bubble()

    listToCompare = []
    current = self.ll_test.head
    while current is not None:
        listToCompare.append(current.getData())
        current = current.getNext()

    self.assertEqual(listToCompare, [1, 2, 3, 4])

  def test_descendingOrder_once(self):
    self.ll_test.add(4)
    self.ll_test.add(3)
    self.ll_test.add(2)
    self.ll_test.add(1)

    self.ll_test.bubble_once()

    listToCompare = []
    current = self.ll_test.head
    while current is not None:
        listToCompare.append(current.getData())
        current = current.getNext()

    self.assertEqual(listToCompare, [3, 2, 1, 4])

  def test_descendingOrder_all(self):
    self.ll_test.add(4)
    self.ll_test.add(3)
    self.ll_test.add(2)
    self.ll_test.add(1)

    self.ll_test.bubble()

    listToCompare = []
    current = self.ll_test.head
    while current is not None:
        listToCompare.append(current.getData())
        current = current.getNext()

    self.assertEqual(listToCompare, [1, 2, 3, 4])

  def test_duplicateElements_once(self):
    self.ll_test.add(1)
    self.ll_test.add(2)
    self.ll_test.add(1)
    self.ll_test.add(4)

    self.ll_test.bubble_once()

    listToCompare = []
    current = self.ll_test.head
    while current is not None:
        listToCompare.append(current.getData())
        current = current.getNext()

    self.assertEqual(listToCompare, [1, 1, 2, 4])

  def test_duplicateElements(self):
    self.ll_test.add(1)
    self.ll_test.add(2)
    self.ll_test.add(1)
    self.ll_test.add(4)

    self.ll_test.bubble()

    listToCompare = []
    current = self.ll_test.head
    while current is not None:
        listToCompare.append(current.getData())
        current = current.getNext()

    self.assertEqual(listToCompare, [1, 1, 2, 4])

  def test_sameNumbers_once(self):
    self.ll_test.add(1)
    self.ll_test.add(1)
    self.ll_test.add(1)
    self.ll_test.add(1)

    self.ll_test.bubble_once()

    listToCompare = []
    current = self.ll_test.head
    while current is not None:
        listToCompare.append(current.getData())
        current = current.getNext()

    self.assertEqual(listToCompare, [1, 1, 1, 1])

  def test_sameNumbers(self):
    self.ll_test.add(1)
    self.ll_test.add(1)
    self.ll_test.add(1)
    self.ll_test.add(1)

    self.ll_test.bubble()

    listToCompare = []
    current = self.ll_test.head
    while current is not None:
        listToCompare.append(current.getData())
        current = current.getNext()

    self.assertEqual(listToCompare, [1, 1, 1, 1])

  def test_oneNode_once(self):
    self.ll_test.add(1)

    self.ll_test.bubble_once()

    listToCompare = []
    current = self.ll_test.head
    while current is not None:
      listToCompare.append(current.getData())
      current = current.getNext()

    self.assertEqual(listToCompare, [1])

  def test_oneNode(self):
    self.ll_test.add(1)

    self.ll_test.bubble()

    listToCompare = []
    current = self.ll_test.head
    while current is not None:
        listToCompare.append(current.getData())
        current = current.getNext()

    self.assertEqual(listToCompare, [1])

  def test_twoOrMore_once(self):
    self.ll_test.add(17)
    self.ll_test.add(79)
    self.ll_test.add(57)
    self.ll_test.add(5)

    self.ll_test.bubble_once()

    listToCompare = []
    current = self.ll_test.head
    while current is not None:
        listToCompare.append(current.getData())
        current = current.getNext()

    self.assertEqual(listToCompare, [17, 57, 5, 79])

  def test_twoOrMore(self):
    self.ll_test.add(17)
    self.ll_test.add(79)
    self.ll_test.add(57)
    self.ll_test.add(5)

    self.ll_test.bubble()

    listToCompare = []
    current = self.ll_test.head
    while current is not None:
        listToCompare.append(current.getData())
        current = current.getNext()

    self.assertEqual(listToCompare, [5, 17, 57, 79])

  def tearDown(self):
      self.ll_test = None

if __name__ == "__main__":
   ll = LinkedList()
   ll.add(4)
   ll.add(3)
   ll.add(2)
   ll.add(1)
   ll.bubble_once()
   print(ll)