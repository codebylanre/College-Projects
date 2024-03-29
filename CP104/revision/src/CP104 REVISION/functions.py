def forloops_multiplication_tableass05n04(start_num, stop_num):
    """
    😭😭😭😭
    -------------------------------------------------------
    Prints a multiplication table for values from start_num to stop_num.
    Use: multiplication_table(start_num, stop_num)
    -------------------------------------------------------
    Parameters:
        start_num - the range start value (int)
        stop_num - the range stop value (int)
    Returns:
        None
    ------------------------------------------------------
    """

    for i in range(start_num, stop_num + 1):
        print(f"   {i:3}", end="")
    print()
    # print("\n -------------")
    print("-"*38)

    for j in range(start_num, stop_num + 1):
        print(f"{j:2}|", end="")
        for j in range(start_num, stop_num+1):
            print(f"{j *i:4}", end="")
        print()

    return

print(forloops_multiplication_tableass05n04(2, 9))