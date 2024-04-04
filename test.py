import unittest
from money import Money

class TestMoney(unittest.TestCase):
    def test_addition(self):
        obj1 = Money(34.31)
        obj2 = Money(45.29)
        obj3 = obj1 + obj2
        self.assertEqual(str(obj3), "79 rupees, 60 paise.\n")
    
    def test_multiplication(self):
        obj1 = Money(34.31)
        obj3 = obj1 * 3
        self.assertEqual(str(obj3), "102 rupees, 93 paise.\n")
    
    def test_subtraction(self):
        obj1 = Money(34.31)
        obj2 = Money(45.29)
        obj3 = obj1 - obj2
        self.assertEqual(str(obj3), "UnderFlow\n\n")
    
    def test_division(self):
        obj1 = Money(34.31)
        obj3 = obj1 / 2
        self.assertEqual(str(obj3), "17 rupees, 16 paise.\n")


if __name__ == "__main__":
    unittest.main()
