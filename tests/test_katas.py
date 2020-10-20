import unittest
import katas
 


class TestKatas(unittest.TestCase):
    def test_add(self):
        self.assertEqual(katas.add(5, 2), 7)
        self.assertEqual(katas.add(-1, 1), 0)
        self.assertEqual(katas.add(-3, 3), 0)
    def test_multiply(self):
        self.assertEqual(katas.multiply(5,2), 10)
        self.assertEqual(katas.multiply(-1, 1), -1)
        self.assertEqual(katas.multiply(-1, -1), 1)
    def test_power(self):
        self.assertEqual(katas.power(5,2), 25)
        self.assertEqual(katas.power(-1, 1), -1)
        self.assertEqual(katas.power(2, 3), 8)
    def test_factorial(self):
        self.assertEqual(katas.factorial(6), 720)
        self.assertEqual(katas.factorial(2), 2)
        self.assertEqual(katas.factorial(3), 6)
    def test_fibonacci(self):
        self.assertEqual(katas.fibonacci(0), 0)
        self.assertEqual(katas.fibonacci(1), 1)
        self.assertEqual(katas.fibonacci(2), 1)


if __name__ == '__main__':
    unittest.main()
