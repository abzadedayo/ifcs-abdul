import unittest
from task1 import fizzBuzz

class TestPerfection(unittest.TestCase):
    def test_happy(self):
        
        assert fizzBuzz(3) == "Fizz"
        assert fizzBuzz(5) == "Buzz"
        assert fizzBuzz(15) == "FizzBuzz"
        

    def test_unhappy(self):
        assert fizzBuzz(6.7) == None

if __name__ == '__main__':
    unittest.main()