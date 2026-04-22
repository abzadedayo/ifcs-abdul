# Fizzbuzz
# Accepts an integer as a parameter
# If multiple of 3, return Fizz
# If multiple of 5, return Buzz
# If multiple of 3 and 5 together, return FizzBuzz
# If not any of these, return None

def fizzBuzz(num):
    # check mul of 3 and 5
    if ((num % 3) == 0) and ((num % 5) == 0):
        return "FizzBuzz"
    #check for mul of 3
    elif ((num % 3) == 0):
        return "Fizz"
    #check for mul of 5
    elif ((num % 5) == 0):
        return "Buzz"
    #if none of these
    else:
        return None
    
# print(fizzBuzz(5))
    