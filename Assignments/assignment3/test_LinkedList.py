import unittest
from LinkedList import LinkedList

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.ll_test = LinkedList()
        self.ll_test.add(1)
        self.ll_test.add(2)
        self.ll_test.add(3)


    def test_delete_repeat(self):
        self.ll_test.delete(0)
        self.ll_test.delete(0)
        self.ll_test.delete(0)

        self.assertEqual(0, self.ll_test.length())

    def test_delete_beginning(self):
        listToCompare = []
        self.ll_test.delete(0)
        
        current = self.ll_test.head
        for i in range(self.ll_test.length()):
            listToCompare.append(current.getData())
            current = current.getNext()

        self.assertEqual(listToCompare, [2, 3])

    def test_delete_middle(self):
        listToCompare = []

        self.ll_test.delete(1)
        
        current = self.ll_test.head
        for i in range(self.ll_test.length()):
            listToCompare.append(current.getData())
            current = current.getNext()

        self.assertEqual(listToCompare, [1, 3])

    def test_delete_end(self):
        listToCompare = []

        self.ll_test.delete(2)
        
        current = self.ll_test.head
        for i in range(self.ll_test.length()):
            listToCompare.append(current.getData())
            current = current.getNext()

        self.assertEqual(listToCompare, [1, 2])

    def test_insert_beginning(self):
        listToCompare = []

        self.ll_test.insert(0, 0)
        
        current = self.ll_test.head
        for i in range(self.ll_test.length()):
            listToCompare.append(current.getData())
            current = current.getNext()

        self.assertEqual(listToCompare, [0, 1, 2, 3])

    def test_insert_middle(self):
        listToCompare = []

        self.ll_test.insert(2, 0)
        
        current = self.ll_test.head
        for i in range(self.ll_test.length()):
            listToCompare.append(current.getData())
            current = current.getNext()

        self.assertEqual(listToCompare, [1, 2, 0, 3])

    def test_insert_end(self):
        listToCompare = []

        self.ll_test.insert(3, 0)
        
        current = self.ll_test.head
        for i in range(self.ll_test.length()):
            listToCompare.append(current.getData())
            current = current.getNext()

        self.assertEqual(listToCompare, [1, 2, 3, 0])


    def tearDown(self):
        self.ll_test = None