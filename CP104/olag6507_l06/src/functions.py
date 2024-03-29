"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Olagunju Abdulbasit
ID:      169076507
Email:   olag6507@mylaurier.ca
__updated__ = "2023-06-26"
-------------------------------------------------------
"""


def sum_even(num):
    """
    -------------------------------------------------------
    Sums and returns the total of all even numbers from 2 to num (inclusive).
    Use: total = sum_even(num)
    -------------------------------------------------------
    Parameters:
        num - an integer (int > 0)
    Returns:
        total - sum of all even numbers from 2 to num (int)
    ------------------------------------------------------
    """

    total = 0
    for i in range(2, num+1, 2):
        total += i
    return total


def draw_triangle(height, char):
    """
    -------------------------------------------------------
    Prints a triangle of height characters using
    the char character.
    Use: draw_triangle(height, char)
    -------------------------------------------------------
    Parameters:
        height - number of characters high (int > 0)
        char - the character to draw with (str, len() == 1)
    Returns:
        None
    ------------------------------------------------------
    """
    i_count = 1
    i_space = height
    for tracker in range(height):
        i_space -= 1
        print(" " * i_space, char * i_count)
        i_count += 2
    return
    #
    # for i in range(1, height + 1):
    #     spaces = " " * (height - i)
    #     triangle = char * (2 * i - 1)
    #     print(spaces + triangle)

    # for i in range(height):
    #     for j in range(height-i-1):
    #         print(" ", end="")
    #     for j in range(2*i+1):
    #         print(char,end="")
    #     print()
    # return


def treadmill(burnt_per_minute, start, end, inc):
    """
    -------------------------------------------------------
    Calculates and prints calories burnt on a treadmill over
    a given time range.
    Use: treadmill(burnt_per_minute, start, end, inc)
    -------------------------------------------------------
    Parameters:
        burnt_per_minute - calories burnt per minute (float > 0)
        start - start time in minutes (int > 0)
        end - end time in minutes (int >= start)
        inc - increment in minutes (int > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    total_calories = 0
    for time in range(start, end + 1, inc):
        calories_burnt = burnt_per_minute * inc
        total_calories += calories_burnt
        print(f"Calories burned after {time:2d} minutes: {total_calories}")
    return


# treadmill(3.9, 5, 30, 5)


def gic(value, years, rate):
    """
    -------------------------------------------------------
    Calculates and prints a table of how much a GIC (Guaranteed
    Income Certificate) is worth over a number of years, and
    returns its final value.
    Use: final_value = gic(value, years, rate)
    -------------------------------------------------------
    Parameters:
        value - GICs initial value (int > 0)
        years - number of years to maturity (int > 0)
        rate - percent increase value per year (float > 0)
    Returns:
        final_value - the final value of the GIC (float)
    ------------------------------------------------------
    """

    for years in range(0, years+1):
        print(f"{years:2d}  {value:4,.2f}")
        final_value = value*(1+(rate/100)**years)
        value = value*(1+(rate/100))

    return final_value


# gic(1000, 25, 2)


def statistics(n):
    """
    -------------------------------------------------------
    Asks a user to enter n values, then calculates and returns
    the minimum, maximum, total, and average of those values.
    Use: minimum, maximum, total, average = statistics(n)
    -------------------------------------------------------
    Parameters:
        n - number of values to process (int > 0)
    Returns:
        minimum - smallest of n values (float)
        maximum - largest of n values (float)
        total - total of n values (float)
        average - average of n values (float)
    ------------------------------------------------------
    """

    # n = int(input("Enter number of values: "))

    # values = int(input("Enter first value: "))
    # total = 0
    # minimum = maximum = values
    #
    # for i in range(n):
    #     values = int(input("Enter next value: "))
    #     total += values
    #     if values > maximum:
    #         maximum = values
    #     if values < minimum:
    #         minimum = values
    #
    # average = total/n
    # print(
    #     f"The total is {total}, the count is {n} and average is {total}")
    # print(f"The maximum is {maximum}, and minimum is {minimum}")

    import math
    values = []

    for i in range(n):
        value = float(input("Enter values: "))
        values.append(value)

    minimum = min(values)
    maximum = max(values)
    total = sum(values)
    average = total/n

    return minimum, maximum, total, average
# I DON'T UNDERSTAND T15 AND SOMETHING WAS WRONG WITH T12 WHILE T06 WAS OUT OF MY LEAGUE
