import unittest
import leapYear

class testBy4(unittest.TestCase):
    def test_one(self):
        self.assertEqual(leapYear.is_leapYear(8), True )

class testNBy4(unittest.TestCase):
    def test_one(self):
        self.assertEqual(leapYear.is_leapYear(9), False )

if __name__ == '__main__':
    unittest.main()