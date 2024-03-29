"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Olagunju Abdulbasit
ID:     169076507
Email:  olag6507@laurier.ca
__updated__ = "Oct 7, 2023"
------------------------------------------------------------------------
"""
from ArrayStack import ArrayStack


# convert Decimal numbers to Binary
dec2bin_stack = ArrayStack()



def divide_by_2(number):
    # Storing the original number before making it positive
    # This would enable us to work with negative code in the future
    keep = number
    
    number = abs(number)

    if number == 0:
        return 0
    
    while number != 0:
        remainder = number % 2
        
        # Push remainder onto stack
        dec2bin_stack.push(str(remainder))
        # print(f"rem {result}")           debugging with print(bad practice tho)
        number //= 2
        # print(number)                    debugging with print
    

    
    bin_string = ""
    
    while not dec2bin_stack.isEmpty():
        bin_string += dec2bin_stack.pop()
     
    # This enables handling of a negative value   
    if keep < 0:
        return f"-{bin_string}"
    else:
        return bin_string
        
        
  
# Test code starts from here  
def testcode():     
    user_input = int(input("Input a number in base 10: "))
    binary_value = divide_by_2(user_input)
    print(f"The binary representation of {user_input} is {binary_value}")
    print()
    user_input = int(input("Input a number in base 10: "))
    binary_value = divide_by_2(user_input)
    print(f"The binary representation of {user_input} is {binary_value}")
    print()
    user_input = int(input("Input a number in base 10: "))
    binary_value = divide_by_2(user_input)
    print(f"The binary representation of {user_input} is {binary_value}")
    
testcode()
        
# One of my favorite CP tasks so far, it's so cool and making it was fun
        
        
        
        
        
        
        
        
        
        