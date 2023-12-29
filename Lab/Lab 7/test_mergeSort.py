import unittest
from MergeSort import merge

# Equivalence Classes: merge two lists, merge one list and empty list, merge two empty lists

class TestMergeSort(unittest.TestCase):
    def setUp(self):
        self.empty_list = []
        self.aList = [3, 5, 7, 8]
        self.aaList = [1, 2, 9, 10]
        self.bList = [2, 4, 5, 7, 9]

    def test_merge_two(self):
        self.assertEqual(merge(self.aList, self.bList), [2, 3, 4, 5, 5, 7, 7, 8, 9])
        
    def test_merge_two_same_length(self):
        self.assertEqual(merge(self.aList, self.aaList), [1, 2, 3, 5, 7, 8, 9, 10])
    def test_merge_one_empty(self):
        self.assertEqual(merge(self.aList, self.empty_list), [3, 5, 7, 8])

    def test_merge_two_empty(self):
        self.assertEqual(merge(self.empty_list, self.empty_list), [])

    def tearDown(self):
        self.empty_list = None
        self.aList = None
        self.bList = None

if __name__ == "__main__":
    unittest.main()