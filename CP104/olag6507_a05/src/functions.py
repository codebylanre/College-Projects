"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Olagunju Abdulbasit
ID:      169076507
Email:   olag6507@mylaurier.ca
__updated__ = "2023-06-29"
-------------------------------------------------------
"""


def factorial(number):
    """
    -------------------------------------------------------
    Calculates and returns the factorial of number.
    Use: product = factorial(number)
    -------------------------------------------------------
    Parameters:
        number - number to factorial (int > 0)
    Returns:
        product - number! (int)
    ------------------------------------------------------
    """
    import math
    products = 1
    for i in range(1, number + 1):
        products *= i
    return products


def calories_counted(per_min, minutes):
    """
    -------------------------------------------------------
    Calculates and returns the number of calories burnt.
    Use: calories_count = calories_counted(per_min, minutes):
    -------------------------------------------------------
    Parameters:
        number - number of calories(float)
    Returns:
        calories counted, minutes
    ------------------------------------------------------
    """

    for i in range(5, minutes+1, 5):
        calories_count = per_min * i
        print(f"{i:2} {calories_count:.1f}")
    return


def arrow_right(width):
    """
    -------------------------------------------------------
    CPrints an arrow of characters
    Use: arrow_right = arrow_right(width)
    -------------------------------------------------------
    Parameters:
        width - width of characters
    Returns:
        characters
    ------------------------------------------------------
    """
    for i in range(width-1):
        for j in range(i):
            print(" ", end="")
        print("#")

    for i in range(width-1, -1, -1):
        for j in range(i):
            print(" ", end="")
        print("#")

    return


def multiplication_table(start_num, stop_num):
    """
    -------------------------------------------------------
    Prints a multiplication table for values from start_num to stop_num.
    Use: multiplication_table(start_num, stop_num)
    -------------------------------------------------------
    Parameters:
        start_num - the range start value (int)
        stop_num - the range stop value (int)
    Returns:
        None
    ------------------------------------------------------
    """

    for i in range(start_num, stop_num + 1):
        print(f"  {i:3}", end="")
    print("\n -------------")

    for j in range(start_num, stop_num + 1):
        print(f"{j:2}|", end="")
        for j in range(start_num, stop_num+1):
            print(f"{j *i:4}", end="")
        print()

    return


def range_sum(start, increment, count):
    """
    -------------------------------------------------------
    Uses a for loop to sum values from start by increment.
    Use: total = range_sum(start, increment, count)
    -------------------------------------------------------
    Parameters:
        start - the range start value (int)
        increment - the range increment (int)
        count - the number of values in the range (int)
    Returns:
        total - the sum of the range (int)
    ------------------------------------------------------
    """
    total = 0
    for i in range(count):
        total += start
        start += increment

    return total
