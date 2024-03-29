"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Olagunju Abdulbasit
ID:      169076507
Email:   olag6507@mylaurier.ca
__updated__ = "2023-07-05"
-------------------------------------------------------
"""
from random import randint


def get_weekday_name(d):
    """
    -------------------------------------------------------
    Returns the name of a day of the week given its number.
    Use: name = get_weekday_name(d)
    -------------------------------------------------------
    Parameters:
        d - day of week number (1 <= int <= 7)
    Returns:
        name - matching day of the week, 1 = "Sunday", 7 = "Saturday" (str)
    -------------------------------------------------------
    """

    days_of_week = ["Sunday", "Monday", "Tuesday",
                    "Wednesday", "Thursday", "Friday", "Saturday"]

    return(days_of_week[d-1])


def generate_integer_list(n, low, high):
    """
    -------------------------------------------------------
    Generates a list of random integers.
    Requires import: from random import randint
    Use: values = generate_integer_list(n, low, high)
    -------------------------------------------------------
    Parameters:
        n - number of values to generate (int, > 0)
        low - low value range (int)
        high - high value range (int, > low)
    Returns:
        values - a list of random integers (list of int)
    -------------------------------------------------------
    """
    # values = []
    # for i in range(n):
    #     value = randint(low, high)
    #     values.append(value)
    # return values

    values = []
    for i in range(n):
        values.append(randint(low, high))
    return values


def list_categorize(values):
    """
    -------------------------------------------------------
    Returns data about the categories of values in a list.
    Use: negatives, positives, zeroes, evens, odds = list_categorize(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of int)
    Returns:
        negatives - the number of negative values (int)
        positives - the number of positive values (int)
        zeroes - the number of zeroes (int)
        evens - the number of even values (int)
        odds - the number of odd values (int)
    -------------------------------------------------------
    """

    negatives = 0
    positives = 0
    zeroes = 0
    evens = 0
    odds = 0

    for i in values:
        if i < 0:
            negatives += 1
        elif i > 0:
            positives += 1
        else:
            zeroes += 1

        if i % 2 == 0:
            evens += 1
        else:
            odds += 1

    return negatives, positives, zeroes, evens, odds
    # for i in values:
    #     if i < 0:
    #         negatives.append(len(i))
    #     if i > 0:
    #         positives.append(len(i))
    #     if i == 0:
    #         zeroes.append(len(i))
    #     if i % 2 == 0:
    #         evens.append(len(i))
    #     if i % 2 != 0:
    #         odds.append(len(i))
    # return negatives, positives, zeroes, evens, odds
    # incorrect application check code below if you want to apply the len code

    # negatives = []
    # positives = []
    # zeroes = []
    # evens = []
    # odds = []
    #
    # for i in values:
    #     if i < 0:
    #         negatives.append(i)
    #     elif i > 0:
    #         positives.append(i)
    #     else:
    #         zeroes.append(i)
    #
    #     if i % 2 == 0:
    #         evens.append(i)
    #     else:
    #         odds.append(i)
    #
    # return len(negatives), len(positives), len(zeroes), len(evens), len(odds)


def union(source1, source2):
    """
    -------------------------------------------------------
    Returns a list that is the union of the contents of source1 and source2.
    Every element that appears at least once in either source1 and source2
    must appear once and only once in target.
    Use: target = union(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a list (list of *)
        source2 - a list (list of *)
    Returns:
        target - the union of source1 and source2 (list of *)
    -------------------------------------------------------
    """

    target = []

    for num in source1 + source2:
        if num not in target:
            target.append(num)

    return target


def symmetric_difference(source1, source2):
    """
    -------------------------------------------------------
    Returns a list that is the symmetric difference of the contents
    of source1 and source2.
    Only elements that appear in one of source1 and source2, but not both,
    appear once and only once in target.
    Use: target = symmetric_difference(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a list (list of *)
        source2 - a list (list of *)
    Returns:
        target - the symmetric difference of source1 and source2 (list of *)
    -------------------------------------------------------
    """

    target = []
    for num in source1:
        if num not in source2 and num not in target:
            target.append(num)

    for num in source2:
        if num not in source1 and num not in target:
            target.append(num)

    return target
