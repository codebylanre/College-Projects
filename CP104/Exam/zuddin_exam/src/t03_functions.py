def alternate_case(string):
    """
    -------------------------------------------------------
    Converts letters in a string to alternate case. Letters
    at an even index are converted to (or left as) upper-case,
    Letters at an odd index are converted to (or left as)
    lower-case. Non-letters are ignored.
    Use: alternating = alternate_case(string)
    -------------------------------------------------------
    Parameters:
        width - maximum width in characters of triangle (int >= 1)
    Returns:
        alternating - the resulting string (str)
    -------------------------------------------------------
    """
    # Your code here
    alternating = ""
    for index, character in enumerate(string):
        if character.isalpha():
            if index % 2 == 0:
                alternating += character.upper()
            else:
                alternating += character.lower()
        else:
            alternating += character

    return alternating