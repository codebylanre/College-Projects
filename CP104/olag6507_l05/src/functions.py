"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Olagunju Abdulbasit
ID:      169076507
Email:   olag6507@mylaurier.ca
__updated__ = "2023-06-13"
-------------------------------------------------------
"""


def closest(target, v1, v2):
    """
    -------------------------------------------------------
    Determines closest value of two values to a target value.
    Use: result = closest(target, v1, v2)
    -------------------------------------------------------
    Parameters:
        target - the target value (float)
        v1 - first comparison value (float)
        v2 - second comparison value (float)
    Returns:
        result - one of v1 or v2 that is closest to target,
          v1 is the value chosen if v1 and v2 are an equal
          distance from target (float)
    -------------------------------------------------------
    """

    distance1 = abs(target - (v1))
    distance2 = abs(target - (v2))

    if distance1 <= distance2:
        result = (v1)
    else:
        result = (v2)
    return result


def is_leap(year):
    """
    Determines if a year is a leap year.
    Use: result = is_leap(year)
    Parameters:
        year - a year (int > 0)
    Returns:
        result - True if year is a leap year,
            False otherwise (boolean)
    """

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                result = True
            else:
                result = False
        else:
            result = True
    else:
        result = False

    return result


'''   
def is_leap(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False
'''


def richter(intensity):
    """
    -------------------------------------------------------
    Determines damage level given earthquake intensity measured
    on the Richter scale.
    Use: result = richter(intensity)
    -------------------------------------------------------
    Parameters:
        intensity - Richter scale number for severity of earthquake
            (float >= 0)
    Returns:
        result - description of earthquake damage (str)
    -------------------------------------------------------
    """
    '''
    if (intensity < 5):
        result = ("Little or no damage")
    elif (intensity >= 5 and intensity < 5.5):
        result = ("Some damage")
    elif (intensity >= 5.5 and intensity < 6.5):
        result = ("Serious damage: walls may crack or fall")
    elif (intensity >= 6.5 and intensity < 7.5):
        result = ("Disaster: buildings may collapse")
    else:
        result = ("Catastrophe: most buildings destroyed")

    return result
    '''  # this is not an optimised code Abdulbasit, do not do this anymore, follow the code below, your code is supposed to be simple
    if (intensity < 5):
        result = ("Little or no damage")
    elif (intensity < 5.5):
        result = ("Some damage")
    elif (intensity < 6.5):
        result = ("Serious damage: walls may crack or fall")
    elif (intensity < 7.5):
        result = ("Disaster: buildings may collapse")
    else:
        result = ("Catastrophe: most buildings destroyed")

    return result


def loan():
    """
    -------------------------------------------------------
    An employee may qualify for a loan if they have worked for a
    minimum of 5 years, and has a salary of $30,000 or more.
    This function must ask for the years employed and the salary
    as appropriate.
    Use: qualified = loan()
    -------------------------------------------------------
    Returns:
        qualified - True if employee qualifies for a loan,
            False otherwise (boolean)
    -------------------------------------------------------
    """
    LEAST_SALARY = 30000
    LEAST_YEARS = 5

    year = int(input("Enter number of years worked: "))
    salary = int(input("Enter salary: "))

    if salary >= LEAST_SALARY:
        if year >= LEAST_YEARS:
            result = True
    else:
        result = False
    return result


def fast_food():
    """
    -------------------------------------------------------
    Food order function.
    Asks user for their order and if they want a combo, and if
    necessary, what is the side order for the combo:
    Prices:
        Burger: $6.00
        Wings: $8.00
        Fries combo: add $1.50
        Salad combo: add $2.00
    Use: price = fast_food()
    -------------------------------------------------------
    Returns:
        price - the price of one meal (float)
    -------------------------------------------------------
    """
    price = 0

    # BURGER = 6
    # WINGS = 8
    # FRIES = 1.5
    # SALAD = 2.0

    order = input("B - burger or W - wings: ")
    combo = input("Make it a combo? (Y/N): ")

    if order == "B":
        price += 6
    elif order == "W":
        price += 8

    if combo == "Y":
        side_order = input("Add fries or Salad: ")
        if side_order == "F":
            price += 1.5
        elif side_order == "S":
            price += 2

    price = float(price)
    return price

print(fast_food())