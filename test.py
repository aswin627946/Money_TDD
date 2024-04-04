import unittest
from money import Money

class TestMoney(unittest.TestCase):
    def test_addition(self):
        obj1 = Money(34.31)
        obj2 = Money(45.29)
        obj3 = obj1 + obj2
        self.assertEqual(str(obj3), "79 rupees, 60 paise.\n")


if __name__ == "__main__":
    unittest.main()
