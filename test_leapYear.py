import unittest
import leapYear

class testBy4(unittest.TestCase):
    def test_one(self):
        self.assertEqual(leapYear.is_leapYear(8), True )

class testNBy4(unittest.TestCase):
    def test_one(self):
        self.assertEqual(leapYear.is_leapYear(9), False )

class testBy100(unittest.TestCase):
    def test_one(self):
        self.assertEqual(leapYear.is_leapYear(200), False )

class testBy400(unittest.TestCase):
    def test_one(self):
        self.assertEqual(leapYear.is_leapYear(400), True )

if __name__ == '__main__':
    unittest.main()