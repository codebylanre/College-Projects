"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Olagunju Abdulbasit
ID:     169076507
Email:  olag6507@laurier.ca
__updated__ = "Oct 26, 2023"
------------------------------------------------------------------------
"""

# Recurisve method to print a from n to 0
def printRecursive(n):
    if n > 0:
        print(n)
        printRecursive(n - 1)

# print(printRecursive(11))


# Factorial with recursive
def RecursiveFactorial(n):
    if n < 1:
        return 1
    return n * RecursiveFactorial(n - 1)

# print(RecursiveFactorial(5))

# Fibonacci with recursion

def fibonacci(n):
    if n <= 2:
        return 1
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

# print(fibonacci(4))

# Fibonacci GPT
def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]  # Initialize the sequence with the first two terms

    while len(fibonacci_sequence) < n:
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)

    return fibonacci_sequence

# Change the value of 'n' to specify how many Fibonacci numbers you want to generate
n = 10  # Change this to the desired number of Fibonacci numbers
fibonacci_sequence = generate_fibonacci(n)

# print("Fibonacci Sequence ({} terms):".format(n))
# print(fibonacci_sequence)

# Recursion on strings

def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:])  + s[0]
    
# print(reverse("Hello"))


# Recursive sum of numbers in a list

def sumlist(list_num):
    if len(list_num) == 0:
        return 0
    else:
        return sumlist(list_num[1:]) + list_num[0]
    

# print(sumlist([1, 2, 3, 4, 5]))

# Recursive function to find the power of an integer

def powerint(n, y):
    if y == 0:
        return 1
    return n * powerint(n, y - 1)

print(powerint(10, 5))