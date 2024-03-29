"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Olagunju Abdulbasit
ID:      169076507
Email:   olag6507@mylaurier.ca
__updated__ = "2023-06-23"
-------------------------------------------------------
"""


def day_of_week(day_num):
    """
    -------------------------------------------------------
    Returns the name of a day of the week given an integer day number.
    Day 1 is Sunday, day 7 is Saturday.
    Returns Error if the number is not valid.
    Use: day = day_of_week(day_num)
    -------------------------------------------------------
    Parameters:
    day_num - day number (1 <= int <= 7)
    Returns:
    day - name of a day of the week (str)
    ------------------------------------------------------
    """

    if day_num == 1:
        day = "Sunday"
    elif day_num == 2:
        day = "Monday"
    elif day_num == 3:
        day = "Tuesday"
    elif day_num == 4:
        day = "Wednesday"
    elif day_num == 5:
        day = "Thursday"
    elif day_num == 6:
        day = "Friday"
    elif day_num == 7:
        day = "Saturday"
    else:
        day = 'ERROR: The number has to be between 1 and 7.'
    return day


def pollution_category(air_quality_index):
    """
    -------------------------------------------------------
    Returns the pollution level given an AQI (Air Quality Index):
        Good - 0 to 50 AQI
        Moderate - 51 - 100 AQI
        Unhealthy for Sensitive Groups - 101 - 150 AQI
        Unhealthy - 151 - 200 AQI
        Very Unhealthy - 201 - 300 AQI
        Hazardous - 300+ AQI
    Returns Error if air_quality_index is negative.
    Use: pollution = pollution_category(air_quality_index)
    -------------------------------------------------------
    Parameters:
        air_quality_index - Air Quality Index (int)
    Returns:
        pollution - name of pollution level (str)
    ------------------------------------------------------
    """

    if air_quality_index < 0:
        pollution = "Air quality index can't be Negative"
    elif air_quality_index < 50:
        pollution = "Good"
    elif air_quality_index <= 100:
        pollution = "Moderate"
    elif air_quality_index <= 150:
        pollution = "Unhealthy for Sensitive Groups"
    elif air_quality_index <= 200:
        pollution = "Unhealthy"
    elif air_quality_index <= 300:
        pollution = "Very Unhealthy"
    elif air_quality_index > 300:
        pollution = "Hazardous"
    else:
        pollution = "Air quality index can't be Negative"
    return pollution


def largest_total(val1, val2, val3):
    """
    -------------------------------------------------------
    Returns the total of the two largest values of
    val1, val2, and val3.
    Use: total = largest_total(val1, val2, val3)
    -------------------------------------------------------
    Parameters:
        val1 - a number (float)
        val2 - a number (float)
        val3 - a number (float)
    Returns:
        total - the total of the two largest values of
            val1, val2, and val3 (float)
    ------------------------------------------------------
    """

    first_largest = val1
    second_largest = val2

    if val2 > first_largest:
        second_largest = first_largest
        first_largest = val2
    elif val2 > second_largest:
        second_largest = val2

    if val3 > first_largest:
        second_largest = first_largest
        first_largest = val3
    elif val3 > second_largest:
        second_largest = val3

    total = first_largest + second_largest
    return total


def colour_blend(rgb_colour1, rgb_colour2):
    """
    -------------------------------------------------------
    Determines the secondary rgb_colour from mixing two primary
    RGB (Red, Green, Blue) colours. The order of the colours
    is *not* significant.
    Returns "Error" if any of the rgb_colour parameter(s) are invalid.
        "red" + "blue": "fuchsia"
        "red" + "green": "yellow"
        "green" + "blue": "aqua"
        "red" + "red": "red"
        "blue" + "blue": "blue"
        "green" + "green": "green"
    Use: rgb_colour = colour_blend(rgb_colour1, rgb_colour2)
    -------------------------------------------------------
    Parameters:
        rgb_colour1 - a primary RGB rgb_colour (str)
        rgb_colour2 - a primary RGB rgb_colour (str)
    Returns:
        rgb_colour - a secondary RGB rgb_colour (str)
    -------------------------------------------------------
    """

    if rgb_colour1 == "red" and rgb_colour2 == "blue" or rgb_colour1 == "blue" and rgb_colour2 == "red":
        rgb_colour = "fuchsia"
    elif rgb_colour1 == "red" and rgb_colour2 == "green" or rgb_colour1 == "green" and rgb_colour2 == "red":
        rgb_Colour = "yellow"
    elif rgb_colour1 == "green" and rgb_colour2 == "blue" or rgb_colour1 == "blue" and rgb_colour2 == "green":
        rgb_colour = "aqua"
    elif rgb_colour1 == "red" and rgb_colour2 == "red":
        rgb_colour = "red"
    elif rgb_colour1 == "blue" and rgb_colour2 == "blue":
        rgb_colour = "blue"
    elif rgb_colour1 == "green" and rgb_colour2 == "green":
        rgb_colour = "green"
    else:
        rgb_colour = "Error"
    return rgb_colour


def hoo_ya(number):
    '''
    hoo_ya takes an integer parameter and returns one of the following strings:
    "Hoo" if number is evenly divisible by 5
    "Ya" if number is evenly divisible by 4
    "Hoo Ya" if number is evenly divisible by both 5 and 4
    "Zilch" if number is none of the above
    '''
    if number % 5 == 0 and number % 4 == 0:
        result = 'Hoo Ya'
    elif number % 5 == 0:
        result = 'Hoo'
    elif number % 4 == 0:
        result = 'Ya'
    else:
        result = 'Zilch'
    return result
