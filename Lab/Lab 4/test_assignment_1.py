import unittest
from assignment_1_solutions import prime_decomposition

class TestFirstAssignment(unittest.TestCase):
    def test_input_less_than_0(self):
        self.assertEqual([], prime_decomposition(0))
    
    def test_repeated_numbers(self):
        self.assertEqual([2, 2, 2], prime_decomposition(8))

    def test_some_repeated_some_not(self):
        self.assertEqual([2, 2, 5], prime_decomposition(20))

    def test_non_repeated_numbers(self):
        self.assertEqual([2, 13], prime_decomposition(26))

    def test_prime_numbers(self):
        self.assertEqual([2], prime_decomposition(2))

if __name__ == "__main__":
    unittest.main