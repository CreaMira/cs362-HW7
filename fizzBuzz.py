def fizzBuzz( input_number ):
    output = ""
    
    if (input_number % 3 == 0):
        output += "Fizz"
    if (input_number % 5 == 0):
        output += "Buzz"
    
    return output
