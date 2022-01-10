# import unittest
from unittest import TestCase
from mymath import power, average, sum

class TestMypackage(TestCase):
    def test_power(self):
        x = power(3, 2)
        self.assertEqual(x, 9)
    
    def test_average(self):
        x = average(10, 20)
        self.assertEqual(x, 15.0)

    def test_sum(self):
        x = sum(10, 20)
        self.assertEqual(x, 30)

# if __name__ == '__main__':
#     unittest.main()
