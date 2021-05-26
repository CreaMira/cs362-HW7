import unittest
import leapYear

class testBy4(unittest.TestCase):
    def test_one(self):
        self.assertEqual(leapYear.is_leapYear(8), True )

if __name__ == '__main__':
    unittest.main()