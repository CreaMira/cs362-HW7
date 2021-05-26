import unittest
import fizzBuzz

class testFizz(unittest.TestCase):
    def test_fizz(self):
        self.assertEqual(fizzBuzz.fizzBuzz(3), "Fizz")

class testBuzz(unittest.TestCase):
    def test_Buzz(self):
        self.assertEqual(fizzBuzz.fizzBuzz(5), "Buzz")

class testFizzBuzz(unittest.TestCase):
    def test_Buzz(self):
        self.assertEqual(fizzBuzz.fizzBuzz(15), "FizzBuzz")

class testTheRest(unittest.TestCase):
    def test_head(self):
        self.assertEqual(fizzBuzz.fizzBuzz(98), 98)


if __name__ == '__main__':
    unittest.main()
