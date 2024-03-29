"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Olagunju Abdulbasit
ID:      169076507
Email:   olag6507@mylaurier.ca
__updated__ = "2023-07-13"
-------------------------------------------------------
"""

"""
Write a function that generates n random integers between
1 and 100 inclusive and returns a count of how many of 
these numbers are even. 
"""




import random
def count_evens(n):
    """
    -------------------------------------------------------
    Generates n random integers and checks each integer whether it is even.
    Use: number_of_evens = count_evens(n)
    -------------------------------------------------------
    Parameters:
        n – number of random integers to be generated (int > 0)
    Returns:
        number_of_evens – count of the even numbers (int)
    -------------------------------------------------------
    """
    # MY RUBBISH CODE LOL
    # def count_evens():
    #
    #     number_of_evens = 0
    #
    #     import random
    #
    #     n = random.int(range(1,101),n)
    #
    #     print n
    #
    #     for i in n:
    #
    #         if i % 2 == 0:
    #
    #             number_of_evens += 1
    #
    # return number_of_evens

# MYPERSONALCORRECTION

def counts_evens(n):
    count = 0
    for i in range(n):
        randomnum = random.randint(1, 101)

        if randomnum % 2 == 0:
            count += 1
    return count


print(counts_evens(50))
