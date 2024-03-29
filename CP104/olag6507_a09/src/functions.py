"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Olagunju Abdulbasit
ID:      169076507
Email:   olag6507@mylaurier.ca
__updated__ = "2023-07-27"
-------------------------------------------------------
"""


def file_head(file_handle, count):
    """
    -------------------------------------------------------
    Prints first count lines of file_handle. Line numbering starts at 0.
    If length of file is shorter than count, stops printing after
    last line of file.
    Use: file_head(file_handle, count)
    -------------------------------------------------------
    Parameters:
        file_handle - file to process (file handle - open for reading)
        count - number of lines to print (int > 0)
    Returns:
        None
    -------------------------------------------------------
    """
    i = 0
    while i < count:
        line = file_handle.readline()
        if not line:
            break
        print(line.strip())
        i += 1
    return
    # for i in range(count):
    #     line = file_handle.readline()
    #     if not line:
    #         break
    #     print(line.strip())


def file_integers(file_handle):
    """
    -------------------------------------------------------
    Extracts positive integers from a file into a list of integers.
    Numbers are comma-delimited. Non-numeric tokens are ignored.
    Use: number_list = file_integers(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - file to process (file handle - open for reading)
    Returns:
        number_list - a list of integers from file_handle (list of int)
    -------------------------------------------------------
    """
    number_list = []
    for line in file_handle:
        for token in line.split(','):
            try:
                number = int(token)
                if number > 0:
                    number_list.append(number)
            except ValueError:
                pass
    return number_list


def file_stats(file_handle):
    """
    -------------------------------------------------------
    Evaluates the contents of a file by counting upper-case letters,
    lower-case letters, digits, white-spaces (including end-of-line
    characters), and remaining characters.
    Use: ucount, lcount, dcount, wcount, rcount = file_stats(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - file to process (file handle - open for reading)
    Returns:
        ucount - The number of upper-case letters in the file (int)
        lcount - The number of lower-case letters in the file (int)
        dcount - The number of digits in the file (int)
        wcount - The number of white-space characters in the file (int)
        rcount - The number of remaining characters in the file (int)
    -------------------------------------------------------
    """
    ucount = 0
    lcount = 0
    dcount = 0
    wcount = 0
    rcount = 0

    for line in file_handle:
        for char in line:
            if char.isupper():
                ucount += 1
            elif char.islower():
                lcount += 1
            elif char.isdigit():
                dcount += 1
            elif char.isspace():
                wcount += 1
            else:
                rcount += 1

    return ucount, lcount, dcount, wcount, rcount


def number_lines(fh_read, fh_write):
    """
    -------------------------------------------------------
    Adds line numbers to a file. Contents of fh_write contain contents
    of fh_read where every line has line numbers added to the beginning
    of the line in the format [number]. Line numbering starts at 0.
    Put a single space after the line number.
    Use: number_lines(fh_read, fh_write)
    -------------------------------------------------------
    Parameters:
        fh_read - file to read (file - open for reading)
        fh_write - file to write (file - open for writing)
    Returns:
        None
    -------------------------------------------------------
    """
    numbering = 0
    for line in fh_read:
        fh_write.write(f"[{numbering}] {line}")
        numbering += 1


def student_info(file_handle):
    """
    -------------------------------------------------------
    Get information from a file of file_handle and grades.
    Use: l_id, h_id, avg = student_info(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - student information file in the format
            surname,forename,id,mark (file - open for reading)
    Returns:
        l_id - the id of the student with the lowest mark (str)
        h_id - the id of the student with the highest mark (str)
        avg - the average mark (float)
    -------------------------------------------------------
    """
    total_marks = 0
    count = 0
    l_id, h_id = None, None
    l_mark, h_mark = float('inf'), float('-inf')

    for line in file_handle:
        surname, forename, student_id, mark = line.strip().split(',')
        mark = float(mark)
        total_marks += mark
        count += 1

        if mark < l_mark:
            l_mark = mark
            l_id = student_id

        if mark > h_mark:
            h_mark = mark
            h_id = student_id

    avg = total_marks / count if count > 0 else 0.0
    return l_id, h_id, avg


# lowest_mark = 100
# highest_mark = 0
# total_mark = 0
# l_id = ""
# h_id = ""
# for line in file_handle:
#     tokens = line.split(',')
#     mark = int(tokens[3])
#     if mark < lowest_mark:
#         lowest_mark = mark
#         l_id = tokens[2]
#     elif mark > highest_mark:
#         highest_mark = mark
#         h_id = tokens[2]
#     total_mark += mark
# avg = total_mark / len(file_handle)
# return l_id, h_id, avg
