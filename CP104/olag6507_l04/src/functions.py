"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Olagunju Abdulbasit
ID:      169076507
Email:   olag6507@mylaurier.ca
__updated__ = "2023-06-06"
-------------------------------------------------------
"""
# Import
import math


# Import

def diameter(radius):
    """
    -------------------------------------------------------
    Calculates and returns diameter of a circle.
    Use: diam = diameter(radius)
    -------------------------------------------------------
    Parameters:
        radius - radius of a circle (float >= 0)
    Returns:
        diam - diameter of a circle (float)
    ------------------------------------------------------
    """

    diam = 2 * radius
    return diam


def pythag(s1, s2):
    """
    -------------------------------------------------------
    Calculates and returns the radius, diameter, circumference,
    and area of circle defined by a right triangle.
    Use: radius, diam, circ, area = pythag(s1, s2)
    -------------------------------------------------------
    Parameters:
        s1 - length of side 1 of a right triangle (float > 0)
        s2 - length of side 2 of a right triangle (float > 0)
    Returns:
        radius - radius of the resulting circle (float)
        diam - diameter of the resulting circle (float)
        circ - circumference of the resulting circle (float)
        area - area of the resulting circle (float)
    ------------------------------------------------------
    """

    hypothenus = math.sqrt(s1**2 + s2**2)

    radius = hypothenus

    diam = 2 * radius

    circ = 2 * math.pi * radius

    area = math.pi * (radius*radius)

    return radius, diam, circ, area


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


def c_to_f(celsius):
    """
    -------------------------------------------------------
    Converts temperatures in celsius to fahrenheit.
    Use: fahrenheit = c_to_f(celsius)
    -------------------------------------------------------
    Parameters:
        celsius - temperature in celsius (int >= -273)
    Returns:
        fahrenheit - equivalent to celsius (float)
    -------------------------------------------------------
    """

    FAHRENHEIT_FREEZING = 32
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


def time_values(seconds):
    """
    -------------------------------------------------------
    Returns seconds in different formats.
    Use: days, hours, minutes = time_values(seconds)
    -------------------------------------------------------
    Parameters:
        seconds - total seconds (int >= 0)
    Returns:
        days - number of days in total_seconds (int >= 0)
        hours - number of hours in total_seconds (int >= 0)
        minutes - number of minutes in total_seconds (int >= 0)
    -------------------------------------------------------
    """

    """
    DO NOT USE THIS CAUSE IT TAKES REMIANDER BUT THE RETURN PARAMETER SAYS
    TOTAL
    #days = seconds//86400
    #seconds = seconds % 86400
    #hours = seconds // 3600
    #minutes = hours % 60
    """
    HOURS_PER_SEC = 3600
    DAYS_PER_SEC = 86400
    MINUTES_PER_SEC = 60

    # THIS IS CORRECT CAUSE IT TAKES NO REMAINDER
    days = seconds//86400
    hours = seconds // 3600
    minutes = seconds//60

    return days, hours, minutes
