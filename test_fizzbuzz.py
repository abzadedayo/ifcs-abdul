from fizzbuzz import fizzBuzz

def test_sample():
    assert 2+2 == 4
    
def test_happy():
    assert fizzBuzz(5) == "Buzz"
    assert fizzBuzz(3) == "Fizz"
    assert fizzBuzz(15) == "FizzBuzz"
    
def test_unhappy():
    assert fizzBuzz(6.7) == None