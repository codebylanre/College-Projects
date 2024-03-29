"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Olagunju Abdulbasit
ID:      169076507
Email:   olag6507@mylaurier.ca
__updated__ = "2023-06-16"
-------------------------------------------------------
"""


def feet_to_acres(square_feet):
    """
    -------------------------------------------------------
    Converts square footage to acres.
    Use: acres = feet_to_acres(square_feet)
    -------------------------------------------------------
    Parameters:
        square_feet - area in square feet (float >= 0)
    Returns:
        acres - square_footage in acres (float)
    ------------------------------------------------------
    """
    SQUARE_FEET_PER_ACRE = 43560

    x = square_feet/43560
    return x


def mow_lawn(width, length, speed):
    """
    -------------------------------------------------------
    Determines how long it takes to mow a rectangular lawn.
    Use: time = mow_lawn(width, length, speed)
    -------------------------------------------------------
    Parameters:
        width - width of a lawn in metres (float > 0)
        length - length of a lawn in metres (float > 0)
        speed - square metres cut per minute (float > 0)
    Returns:
        time_minutes - time required to mow the lawn (float)
    ------------------------------------------------------
    """

    time_minutes = (width * length)/speed
    return time_minutes


def date_extract(date_number):
    """
    -------------------------------------------------------
    Extracts the year, month, and day from a date number in the format DDMMYYYY.
    Use: year, month, day = date_extract(date_number)
    -------------------------------------------------------
    Parameters:
        date_number - a date number in the format DDMMYYYY (int)
    Returns:
        year - year portion of date_number (int)
        month - month portion of date_number (int)
        day - day portion of date_number (int)
    ------------------------------------------------------
    """
    month = date_number // 1000000
    day = (date_number // 10000) % 100
    year = date_number % 10000

    result = year, day, month
    return result


def fraction_product(num1, den1, num2, den2):
    """
    -------------------------------------------------------
    Calculates and returns fraction values.
    Use: num, den, product = fraction_product(num1, den1, num2, den2)
    -------------------------------------------------------
    Parameters:
        num1 - numerator of first fraction (int)
        den1 - denominator of first fraction (int != 0)
        num2 - numerator of second fraction (int)
        den2 - denominator of second fraction (int != 0)
    Returns:
        num - numerator of product (int)
        den - denominator of product (int)
        product - num / den (float)
    -------------------------------------------------------
    """

    num = num1 * num2
    den = den1 * den2
    product = num/den
    return num, den, product


def falling_time(distance):
    """
    -------------------------------------------------------
    Calculates time an object takes to fall a certain distance
    due to gravity.
    Use: time = falling_time(distance)
    -------------------------------------------------------
    Parameters:
        distance - distance object has fallen in metres (int >= 0)
    Returns:
        time - time object takes to fall in seconds (float)
    -------------------------------------------------------
    """
    import math
    G = 9.8

    time = math.sqrt((2*distance)/G)

    return time
