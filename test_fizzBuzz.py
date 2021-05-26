import unittest
import fizzBuzz

class testCaseAdd(unittest.TestCase):
    def test_fizz(self):
        self.assertEqual(fizzBuzz.fizzBuzz(3), "Fizz")

if __name__ == '__main__':
    unittest.main()
