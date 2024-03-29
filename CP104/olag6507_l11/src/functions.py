"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Olagunju Abdulbasit
ID:      169076507
Email:   olag6507@mylaurier.ca
__updated__ = "2023-07-24"
-------------------------------------------------------
"""
import random


def generate_matrix_num(rows, cols, low, high, value_type):
    """
    -------------------------------------------------------
    Generates a 2D list of numbers of the given type, 'float' or 'int'.
    (To generate random float number use random.uniform and to
    generate random integer number use random.randint)
    Use: matrix = generate_matrix_num(rows, cols, low, high, value_type)
    -------------------------------------------------------
    Parameters:
        rows - number of rows in the list (int > 0)
        cols - number of columns (int > 0)
        low - low value of range (float)
        high - high value of range (float > low)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        matrix - a 2D list of random numbers (2D list of float/int)
    -------------------------------------------------------
    """
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            # generate a value and append in current row
            if value_type == "int":
                number = random.randint(low, high)
            else:
                number = random.uniform(low, high)
            row.append(number)
        matrix.append(row)
    return matrix


def generate_matrix_char(rows, cols):
    """
    -------------------------------------------------------
    Generates a 2D list of random lower case letter ('a' - 'z') values
    Use: matrix = generate_matrix_char(rows, cols)
    -------------------------------------------------------
    Parameters:
        rows - number of rows in the generated matrix (int > 0)
        cols - number of columns in the generated matrix (int > 0)
    Returns:
        matrix - a 2D list of random characters (2D list of str)
    -------------------------------------------------------
    """
    matrix = []
    for i in range(rows):
        rows = []
        for j in range(cols):
            char = chr(random.randint(97, 122))
            rows.append(char)
        matrix.append(rows)
    return matrix
    # try to understand this code and it's line 63 better, inorder to be able to apply this in future code


def matrix_stats(matrix):
    """
    -------------------------------------------------------
    Returns statistics on a 2D list.
        Use: smallest, largest, total, average = matrix_stats(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of numbers (2D list of float/int)
    Returns:
        smallest - the smallest number in matrix (float/int)
        largest - the largest number in matrix (float/int)
        total - the total of the numbers in matrix (float/int)
        average - the average of numbers in matrix (float/int)
    -------------------------------------------------------
    """


    item = [i for sublist in matrix for i in sublist]
    smallest = min(item)
    largest = max(item)
    total = sum(item)
    average = total / len(item)
    return smallest, largest, total, average

    # smallest = min(item for sublist in matrix for item in sublist)
    # largest = max(item for sublist in matrix for item in sublist)
    # total = sum(item for sublist in matrix for item in sublist)
    # average = total/len(matrix[0])
    # return smallest, largest, total, average


def matrix_scalar_multiply(matrix, num):
    """
    -------------------------------------------------------
    Update matrix by multiplying each element of matrix by num.
    Use: matrix_scalar_multiply(matrix, num)
    -------------------------------------------------------
    Parameters:
        matrix - the matrix to multiply (2D list of int/float)
        num - the number to multiply by (int/float)
    Returns:
        None
    ------------------------------------------------------
    """

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] *= num

    return


def matrix_equal(matrix1, matrix2):
    """
    -------------------------------------------------------
    Compares two matrices to see if they are equal - i.e. have the
    same contents in the same locations.
    Use: equal = matrix_equal(matrix1, matrix2)
    -------------------------------------------------------
    Parameters:
        matrix1 - the first matrix (2D list of *)
        matrix2 - the second matrix (2D list of *)
    Returns:
        equal - True if matrix1 and matrix2 are equal,
            False otherwise (boolean)
    ------------------------------------------------------
    """

    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        result = False
    
    result = True
    for i in range(len(matrix1)):
        for j in range(len(matrix1[i])):
            if matrix1[i][j] != matrix2[i][j]:
                result = False
    return result
    # equal = False
    # rows, cols = len(matrix1), len(matrix2[0])
    # all([matrix1[x][y] == matrix2[x][y]
    #      for y in range(cols) for x in range(rows)])
    # if matrix1 == matrix2:
    #     equal = True
    # return equal
