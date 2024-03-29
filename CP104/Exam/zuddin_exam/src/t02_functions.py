# from debugpy._vendored.pydevd.pydevd_attach_to_process.winappdbg.win32.defines import TRUE,\
#     FALSE
# from turtledemo.__main__ import MINIMUM_FONT_SIZE
def prime_stats(numbers):
    """
    -------------------------------------------------------
    Finds the prime numbers from a list of numbers, and calculates the count, maximum, minimum, and average of those prime numbers.
    A prime number is a positive integer greater than 1 that has no positive integer divisors other than 1 and itself. 
    To find whether a number is prime, you may run a loop from 2 to the square root of the number (inclusive) 
    and check if any integer in the loop divides that number. 
    Use: primes, count, maximum, minimum, average = prime_stats(numbers)
    -------------------------------------------------------
    Parameters:
        numbers - a list of numbers containing both prime and composite numbers (list of int)
    Returns:
        primes - all primes in the list
        count - number of primes in the list
        maximum - the maximum prime in the list
        minimum - the minimum prime in the list
        average - average of primes in the list
    -------------------------------------------------------
    """
    # Your code here
    primes = []
    for number in numbers:
        prime = True  
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                prime = False
                break
        if prime:
            primes.append(number)
    
    count = len(primes)
    if count == 0:
        maximum = minimum = average = 0  #for cases of an empty list
    else:
        maximum = max(primes)
        minimum = min(primes)
        average = sum(primes) / count

    return primes, count, maximum, minimum, average


    
    
    
    
    
    
    
    
    
    
