#Fizzbuzz
# multiple of 3 fizz, multiple of 5 buzz, both FizzBuzz, none return error
def fizzBuzz(num):
    if ((num % 3) == 0) and ((num % 5) == 0):
        return "FizzBuzz"
    elif (num % 3) == 0:
        return "Fizz"
    elif (num % 5) == 0:
        return "Buzz"
    else:
        # new_num = int(input("Type a new number"))
        # return(fizzBuzz(new_num))
        return None
