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


def list_all_factors(number):
    """
    -------------------------------------------------------
    Returns a list of factors for a given number.
    use: list = list_all_factors(number)
    -------------------------------------------------------
    Parameters:
        number (int): The integer for which to find the factors.
    Returns:
        A list of factors of the given number, excluding the number itself.
    -------------------------------------------------------
    """

    factors = []
    for i in range(1, number):
        if number % i == 0:
            factors.append(i)
    return factors


def positive_numbers():
    """
    -------------------------------------------------------
    Gets a list of positive numbers from a user.
    Negative numbers are ignored. Enter 0 to stop entries.
    Use: number_list = positive_numbers()
    -------------------------------------------------------
    Returns:
        number_list - A list of positive integers (list of int)
    ------------------------------------------------------
    """
    positive = []
    number = int(input("Enter a positive number: "))
    while number != 0:
        if number > 0:
            positive.append(number)
        number = int(input("Enter a positive number: "))
    return positive


def list_indexes(numbers, target_number):
    """
    -------------------------------------------------------
    Finds the indexes of target_number in numbers.
    Use: index_list = list_indexes(numbers, target_number)
    -------------------------------------------------------
    Parameters:
        numbers - list of values (list)
        target_number - value to look for in num_list (*)
    Returns:
        index_list - list of indexes of target_number (list of int)
    -------------------------------------------------------
    """
    index = []
    for i in range(len(numbers)):
        if numbers[i] == target_number:
            index.append(i)
    return index

    # for char in numbers:
    #     if char == target_number:
    #         return(len(char))


def subtract_lists(minuend, subtrahend):
    """
    -------------------------------------------------------
    Alters the contents of minuend so that it does not contain
    any values in subtrahend.
    i.e. the values in the first list that appear in the second list
    are removed from the first list.
    Use: subtract_lists(minuend, subtrahend)
    -------------------------------------------------------
    Parameters:
        minuend - a list of values (list)
        subtrahend - a list of values to not include in difference (list)
    Returns:
        None
    ------------------------------------------------------
    """
    indexes = []
    for i in range(len(minuend)):
        if minuend[i] in subtrahend:
            indexes.append(i)
    for index in reversed(indexes):
        minuend.pop(index)
    return
    # for i in range(len(minuend)):
    #     if subtrahend[i] == minuend[i]:
    #         minuend.remove(i)
    # return minuend


def is_sorted(numbers):
    """
    -------------------------------------------------------
    Determines whether a list is sorted.
    Use: in_order, index = is_sorted(numbers)
    -------------------------------------------------------
    Parameters:
        numbers - a list of numbers (list)
    Returns:
        in_order - True if numbers is sorted, False otherwise (bool)
        index - index of first value not in order,
            -1 if in_order is True (int)
    ------------------------------------------------------
    """
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            result = False, i + 1

    result = True, -1
    return result
