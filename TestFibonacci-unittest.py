import unittest
from Fibonacci import fibonacci_series

class TestFibonacciSeries(unittest.TestCase):
    def test_fibonacci_series(self):
        self.assertEqual(fibonacci_series(1), [0])
        self.assertEqual(fibonacci_series(2), [0, 1])
        self.assertEqual(fibonacci_series(5), [0, 1, 1, 2, 3])
        self.assertEqual(fibonacci_series(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])

if __name__ == '__main__':
    unittest.main()