def closest_number(values, target):
    """
    -------------------------------------------------------
    Returns the number that is closest to target in a list of values. 
    If multiple values are closest to target, return the first one.
    Returns 0 if the list is empty.
    Use: cn = closest_number(values, target)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of int)
    Returns:
        cn - the closest number to target in a list of values (int)
    -------------------------------------------------------
    """
    # Your code here
    if len(values) == 0:
        return 0
    closest_number = values[0]
    closest_difference = abs(closest_number - target)
    
    for value in values:
        differences = abs(value - target)
        if differences < closest_difference:
            closest_number = value
            closest_difference = differences
    return closest_number
        