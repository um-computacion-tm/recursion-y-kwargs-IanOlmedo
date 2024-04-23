import unittest
from cuentas import sumatoria1, sumatoria2

class TestSumatorias(unittest.TestCase):

    def test_sumatoria1(self):
        self.assertEqual(sumatoria1(7), 28)
        self.assertEqual(sumatoria1(10), 55)
        self.assertEqual(sumatoria1(1), 1)

    def test_sumatoria2(self):
        self.assertEqual(sumatoria2(6), 21)
        self.assertEqual(sumatoria2(10), 55)
        self.assertEqual(sumatoria2(1), 1)

if __name__ == '__main__':
    unittest.main()
