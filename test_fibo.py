import unittest
from cuentas import fibonacci, fibonacci2, fibonacci3

class TestFibonacci(unittest.TestCase):

    def test_fibonacci(self):
        self.assertEqual(fibonacci(13), 233)
        self.assertEqual(fibonacci(7), 13)
        self.assertEqual(fibonacci(1), 1)

    def test_fibonacci2(self):
        self.assertEqual(fibonacci2(4), 3)
        self.assertEqual(fibonacci2(6), 8)
        self.assertEqual(fibonacci2(1), 1)

    def test_fibonacci3(self):
        self.assertEqual(fibonacci3(13), 233)
        self.assertEqual(fibonacci3(8), 21)
        self.assertEqual(fibonacci3(1), 1)

if __name__ == '__main__':
    unittest.main()
