"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Olagunju Abdulbasit
ID:      169076507
Email:   olag6507@mylaurier.ca
__updated__ = "2023-06-28"
-------------------------------------------------------
"""


from random import randint


# def hi_lo_game(high):
#     """
#     -------------------------------------------------------
#     Plays a random higher-lower guessing game.
#     Use: count = hi_lo_game(high)
#     -------------------------------------------------------
#     Parameters:
#         high - maximum random value (int > 1)
#     Returns:
#         count - the number of guesses the user made (int)
#     -------------------------------------------------------
#     """
#     number = randint(1, high)
#     count = 1
#     guess = int(input("Guess: "))
#     while number != guess:
#         if guess < number:
#             print("Too low, try again.")
#         elif guess > number:
#             print("Too high, try again.")
#         guess = int(input("Guess: "))
#         count += 1
#     return count


def hi_lo_game(high):
    """
    -------------------------------------------------------
    Plays a random higher-lower guessing game.
    Use: count = hi_lo_game(high)
    -------------------------------------------------------
    Parameters:
        high - maximum random value (int > 1)
    Returns:
        count - the number of guesses the user made (int)
    -------------------------------------------------------
    """
    number = randint(1, high)
    count = 0

    while True:
        guess = int(input("Guess: "))
        count += 1

        if guess > number:
            print("Too high, try again.")
        elif guess < number:
            print("Too low, try again.")
        else:
            print("Congratulations - good guess!")
            break

    print("You made", count, "guesses.")
    return count


def population_growth(target, current, rate):
    """
    -------------------------------------------------------
    Determines the number of years to reach a target population.
    Use: years = population_growth(target, current, rate)
    -------------------------------------------------------
    Parameters:
        target - target population (int > current)
        current - current population (int > 1)
        rate - percent rate of growth (float > 0)
    Returns:
        years - the number of years to reach target population (int)
    -------------------------------------------------------
    """
    years = 0
    while current < target:
        current += current * (rate/100)
        years += 1
    return years


def positive_statistics():
    """
    -------------------------------------------------------
    Asks a user to enter a series of positive numbers, then calculates
    and returns the minimum, maximum, total, and average of those numbers.
    Stop processing values when the user enters a negative number.
    The first number entered must be positive.
    Use: minimum, maximum, total, average = positive_statistics()
    -------------------------------------------------------
    Returns:
        minimum - smallest of the entered values (float)
        maximum - largest of the entered values (float)
        total - total of the entered values (float)
        average - average of the entered values (float)
    ------------------------------------------------------
    """

    numbers = float(input("Enter positive value: "))
    maximum = minimum = numbers
    count = 0
    total = 0
    while numbers > -1:
        count += 1
        total += numbers
        if numbers > maximum:
            maximum = numbers
        if numbers < minimum:
            minimum = numbers
        numbers = float(input("Next positive value: "))
    average = total/count

    return minimum, maximum, total, average


def meal_costs():
    """
    -------------------------------------------------------
    Asks a user the costs of breakfast, lunch, and supper for each
    day the user was away. Assumes there is at least one day, and
    after entering data for each day asks the user whether they want
    to enter data for another day. Calculates total costs for meals.
    Use: b_total, l_total, s_total, a_total = meal_costs()
    -------------------------------------------------------
    Returns:
        b_total - total breakfasts cost (float)
        l_total - total lunches cost (float)
        s_total - total suppers cost (float)
        a_total - all meals cost (float)
    ------------------------------------------------------
    """
    b_total = 0
    l_total = 0
    s_total = 0
    a_total = 0
    day = 1
    while True:
        print(f"For Day {day}")
        print()
        breakfast = float(input("How much was breakfast? $"))
        lunch = float(input("How much was lunch? $"))
        supper = float(input("How much was supper? $"))
        total_meal = breakfast + lunch + supper

        print(f"Your total for the day was ${total_meal:.2f}")
        print()
        b_total += breakfast
        l_total += lunch
        s_total += supper
        a_total += total_meal

        question = input("Were you away for another day (Y/N)? ")
        print()
        if question == "N":
            break

        day += 1

    # a_total = b_total + l_total + s_total
    return b_total, l_total, s_total, a_total


def get_int(low, high):
    """
    -------------------------------------------------------
    Asks a user for an integer value between low and high, and
    continues asking until an acceptable value is input.
    Use: value = get_int(low, high)
    -------------------------------------------------------
    Parameters:
        low - the lowest acceptable integer (inclusive) (int)
        high - the higest acceptable integer (inclusive) (int > low)
    Returns:
        value - a number between low and high (int)
    ------------------------------------------------------
    """
    value = int(input(f"Enter a value between {low} and {high}: "))

    while True:
        if value < low:
            print("Value entered is too low")
        elif value > high:
            print("Value entered is too high")
        else:
            break

        value = int(input(f"Enter a value between {low} and {high}: "))
    return value

    # number = randint(low, high)
    # Value = int(input(f"Enter a value between {low} and {high}: "))
    # while True:
    #
    #
    #     if Value < number:
    #         print("Value entered is too low: ")
    #         Value = int(input(f"Enter a value between {low} and {high}: "))
    #     elif Value > number:
    #         print("Value entered is too high: ")
    #         Value = int(input(f"Enter a value between {low} and {high}: "))
    #     else:
    #         break
    # return number
