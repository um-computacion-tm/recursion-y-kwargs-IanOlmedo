import unittest
from cuentas import factorial, factorial2

class TestFactorial(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(6), 720)
        self.assertEqual(factorial(1), 1)

    def test_factorial2(self):
        self.assertEqual(factorial2(3), 6)
        self.assertEqual(factorial2(5), 120)
        self.assertEqual(factorial2(0), 1)

if __name__ == '__main__':
    unittest.main()
