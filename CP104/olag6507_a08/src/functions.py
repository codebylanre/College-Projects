"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Olagunju Abdulbasit
ID:      169076507
Email:   olag6507@mylaurier.ca
__updated__ = "2023-07-20"
-------------------------------------------------------
"""
import re


def spaced_string(sentence):
    """
    -------------------------------------------------------
    Create a new sentence with added space between words. Words start
    with upper-case characters.
    Use: spaced = spaced_string(sentence)
    -------------------------------------------------------
    Parameters:
        sentence - sentence that represents a sentence in which all the
            words are run together (no spaces), but the first character
            of each word is uppercase. sentence has at least one
            character (str)
    Returns:
        spaced - new sentence in which the words are separated
            by spaces and only the first word starts with
            an uppercase character (str)
    -------------------------------------------------------
    """
    spaced = sentence[0]  # First word starts with uppercase

    # Loop through each character in the sentence, starting from the second character
    for i in range(1, len(sentence)):
        # If the current character is uppercase, it indicates the start of a new word
        if sentence[i].isupper():
            # Add a space before the uppercase character
            spaced += " " + sentence[i].lower()
        else:
            # Append the current character to the current word
            spaced += sentence[i].lower()

    # Return the final spaced sentence
    return spaced

    # stringlist = []
    # stringlist.append(sentence)
    # stringlist2 = []
    # for element in stringlist:
    #     double = [[]]
    #     for char in element:
    #         if char.isupper():
    #             double.append([])
    #         double[-1].append(char)
    #     stringlist2.append(' '.join(''.join(element) for element in double))
    #     new_string = ""
    #     for element in stringlist2:
    #         new_string += element
    #         new_string_1 = new_string[1].capitalize()
    #         new_string_2 = new_string[2:].lower()
    #         new_string = new_string_1 + new_string_2
    #         new_string = new_string.lstrip()
    # return new_string

    # spaced = ""
    # for word in words:
    #     first_letter = word[0]
    #     rest_of_word = word[1:]
    #     spaced += first_letter.upper() + rest_of_word.lower()
    #
    #     return spaced

    # Initialize an empty string to store the spaced sentence
    # spaced = ""
    # # Loop through each character in the sentence
    # for i in range(len(sentence)):
    #     # If the current character is uppercase (indicating the start of a new word)
    #     if sentence[i].isupper():
    #         # If this is not the first word, add a space before it
    #         if i > 0:
    #             spaced += " "
    #     # Append the current character to the spaced string
    #     spaced += sentence[i]
    #
    # # Return the final spaced sentence
    # return spaced


def pluralized_string(string):
    """
    -------------------------------------------------------
    Pluralizes a string according to the rules:
        - if string ends with 's', 'sh', or 'ch', add 'es'
        - if string ends with 'y' but not 'ay' or 'oy', replace
            the 'y' with 'ies'
        - otherwise add 's'
    Use: pluralized = pluralized_string(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        pluralized - a pluralized_string version of string (str)
    -------------------------------------------------------
    """
    # Check if the string ends with 's', 'sh', or 'ch'
    if string.endswith(('s', 'sh', 'ch')):
        pluralized = string + 'es'
    # Check if the string ends with 'y' but not 'ay' or 'oy'
    elif string.endswith('y') and not string.endswith(('ay', 'oy')):
        pluralized = string[:-1] + 'ies'
    else:
        pluralized = string + 's'

    return pluralized


def common_ending(str1, str2):
    """
    -------------------------------------------------------
    Returns the longest common ending of two strings.
    Use: suffix = common_ending(str1, str2)
    -------------------------------------------------------
    Parameters:
        str1 - first string for ending comparison (str)
        str2 - second string for ending comparison (str)
    Returns:
        suffix - the longest common ending of str1 and str2 (str)
    -------------------------------------------------------
    """
    # Initialize two variables: str1 and common_end.
    str1 = str1.lstrip()
    common_end = str1
    # Loop until str2 ends with str1.
    while not str2.endswith(str1):
        # Remove the first character from str1.
        str1 = str1[1:]
        # Update common_end
        common_end = str1
        # Return the value of common_end.
    return common_end


def is_isbn(isbn):
    """
    -------------------------------------------------------
    Determines if an ISBN string is valid. An ISBN string is valid if:
        - it consists of only digits and dashes ('-')
        - it contains 5 groups of digits separated by dashes
        - its first group of digits is either '978' or '979'
        - its final group of digits is a single digit
        - its entire length is 17 characters
    Use: is_valid = is_isbn(isbn)
    -------------------------------------------------------
    Parameters:
        isbn - a string (str)
    Returns:
        is_valid - True if isbn is valid, False otherwise (boolean)
    -------------------------------------------------------
    """
    # # Initialize a variable to store the validity of the ISBN.
    # is_valid = True
    #
    # # Check if the ISBN string is only digits and dashes.
    # if not isbn.isalnum():
    #     is_valid = False
    #
    # # Check if the ISBN string contains 5 groups of digits separated by dashes.
    # if len(isbn) != 17 or "-" not in isbn:
    #     is_valid = False
    #
    # # Check if the first group of digits is either '978' or '979'.
    # if isbn[:3] not in ("978", "979"):
    #     is_valid = False
    #
    # # Check if the final group of digits is a single digit.
    # if not isbn[-1].isdigit():
    #     is_valid = False
    #
    # return is_valid

    # Define the regular expression pattern to match the ISBN format
    isbn_pattern = r'^978-?\d{1,5}-?\d{1,7}-?\d{1,7}-?\d$'

    # Use the re.match function to check if the entire ISBN matches the pattern
    is_valid = bool(re.match(isbn_pattern, isbn))

    return is_valid


def is_word_chain(words):
    """
    -------------------------------------------------------
    Determines if a list of strings is a word chain. A word chain
    is a list of words in which the last character of a word in
    the list is the same as the first character of the next word
    in the list.
    Use: word_chain = check_word_chain(words)
    -------------------------------------------------------
    Parameters:
        words - a of strings (list of str, len > 1)
    Returns:
        word_chain - True if words is a word chain,
            False otherwise (boolean)
    -------------------------------------------------------
    """
    # Initialize a variable to store the validity of the word chain.
    word_chain = True
    current_word = words[0]

    # Check if the word chain is valid.
    i = 1
    while i < len(words):

        # Check if the first character of the word is the same
        # as the last character of the word chain.
        if words[i][0] != current_word[-1]:
            word_chain = False
            break

        # Update the current word.
        current_word = words[i]
        i += 1

    return word_chain
    # Initialize a list to store the words in the word chain.
    # lst = []
    #
    # # Add the first word to the word chain.
    # lst.append(words[0])
    #
    # # Check if the word chain is valid.
    # word_chain = True
    # for word in words:
    #
    #     # Check if the first character of the word is the same
    #     # as the last character of the word chain.
    #     if word[0] != lst[-1][-1]:
    #         word_chain = False
    #         break
    #
    #     # Add the word to the word chain.
    #     lst.append(word)
    #
    # return word_chain
