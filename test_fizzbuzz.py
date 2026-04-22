from fizzbuzz import fizzBuzz

def test_happy():
    assert fizzBuzz(3) == "Fizz"
    assert fizzBuzz(5) == "Buzz"
    assert fizzBuzz(30) == "FizzBuzz"
    
def test_unhappy():
    assert fizzBuzz(5.1) == None
