# FizzBuzz
# multiples of 3 should return "Fizz"
# multiples of 5 should return "Buzz"
# multiples of 3 and 5 together return "FizzBuzz"

def fizzBuzz(num):
    # check for both
    if ((num % 3) == 0) and ((num % 5) == 0):
        return "FizzBuzz"
    #check for multiple of 3
    elif (num % 3) == 0:
        return "Fizz"
    #check for a multiple of 5
    elif (num % 5) == 0:
        return "Buzz"
    #check for none
    else:
        return None
    
# print(fizzBuzz(5))