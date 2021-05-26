import unittest
import fizzBuzz

class testFizz(unittest.TestCase):
    def test_fizz(self):
        self.assertEqual(fizzBuzz.fizzBuzz(3), "Fizz")

class testBuzz(unittest.TestCase):
    def test_buzz(self):
        self.assertEqual(fizzBuzz.fizzBuzz(5), "Buzz")

if __name__ == '__main__':
    unittest.main()
