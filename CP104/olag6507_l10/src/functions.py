"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Olagunju Abdulbasit
ID:      169076507
Email:   olag6507@mylaurier.ca
__updated__ = "2023-07-17"
-------------------------------------------------------
"""


def customer_record(fh, n):
    """
    -------------------------------------------------------
    Find the n-th record in a comma-delimited sequential file.
    Records are numbered starting with 0.
    Use: result = customer_record(fh, n)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
        n - the number of the record to return (int > 0)
    Returns:
        result - a list of the fields of the n-th record if it exists,
            an empty list otherwise (list)
    -------------------------------------------------------
    """
    result = []
    line = fh.readline()
    i = 0
    while line != "" and i <= n:
        if i == n:
            result = line.strip().split(",")
            # line = line.strip
            # result.append(line.strip())
            break
        i += 1
        line = fh.readline()

    return result


def customer_by_id(fh, id_number):
    """
    ------------------------'-------------------------------
    Find the record for a given ID in a sequential file.
    Use: result = customer_by_id(fh, id_number)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
        id_number - the id_number to match (str)
    Returns:
        result - the record with id_number if it exists,
            an empty list otherwise (list)
    -------------------------------------------------------
    """
    result = []
    line = fh.readline()
    while line != "":
        records = line.strip().split(",")
        if records[0] == id_number:
            result = records
            break
        line = fh.readline()
    return result


def number_stats(fh):
    """
    -------------------------------------------------------
    Returns statistics on the numbers in a file.
    Assumes file is not empty.
    Use: smallest, largest, total, average = number_stats(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
    Returns:
        smallest - smallest number (int)
        largest - largest number (int)
        total - sum of all the numbers in the file (int)
        average - average of all the numbers (float)
    ------------------------------------------------------
    """
    line = fh.readline()
    first = int(line.strip())
    smallest = first
    largest = first
    total = first
    counter = 1
    line = fh.readline()

    while line != "":
        counter += 1
        second = int(line.strip())
        if smallest > second:
            smallest = second
        if largest < second:
            largest = second
        total += second
        line = fh.readline()

    average = total / counter
    return smallest, largest, total, average
    # minimum = float('inf')
    # maximum = float('-inf')
    # total = 0
    # count = 0
    #
    # for line in fh:
    #     number = line.strip()
    #     if number.isdigit():
    #         number = int(number)
    #         if number < minimum:
    #             minimum = number
    #         if number > maximum:
    #             maximum = number
    #         total += number
    #         count += 1
    #
    # average = total / count if count > 0 else 0
    #
    # return minimum, maximum, total, average


def count_frequency_value(fh, value):
    """
    -------------------------------------------------------
    Counts the number of appearances of value in fh.
    Use: count = count_frequency_value(fh, value)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
        value - the value to count (int)
    Returns:
        count - the number of appearance of value in fh (int)
    ------------------------------------------------------
    """
    count = 0
    for line in fh:
        line = line.strip()
        numbers = line.split()

        for number in numbers:
            if int(number) == value:
                count += 1

    return count


def find_shortest(fh):
    """
    -------------------------------------------------------
    Finds the first word with shortest length in fh.
    Assumes file is not empty.
    Use: word = find_shortest(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
    Returns:
        word - the first word with the shortest length in fh (str)
    ------------------------------------------------------
    """

    shortest_word = ""
    shortest_length = -1
    first_word = True

    for line in fh:
        line = line.strip()
        words = line.split()  # Split the line into individual words

        for word in words:
            word_length = len(word)
            if first_word or word_length < shortest_length:
                shortest_word = word
                shortest_length = word_length
                first_word = False

    return shortest_word
