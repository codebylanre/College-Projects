"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Olagunju Abdulbasit
ID:      169076507
Email:   olag6507@mylaurier.ca
__updated__ = "2023-07-08"
-------------------------------------------------------
"""


def choose_winner():
    """
    ------------------------------------------------------
    choose_winner takes no parameters and asks the user to enter
    a series of strings that represent the output of 
    a game with a loopUse: winner = choose_winner(string)
    -------------------------------------------------------
    Returns:
       count 
    ------------------------------------------------------
    """
    red = 0
    green = 0
    while True:
        question = input("Enter the winning team:")
        if question == "":
            break
        elif question == "red":
            red += 1
        elif question == "green":
            green += 1

    return red, green


def is_prime(number):
    """
    -------------------------------------------------------
    Determines if number is a prime number.
    Use: prime = is_prime(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int > 1)
    Returns:
        prime - True if number is prime, False otherwise (bool)
    ------------------------------------------------------
    """

    if number <= 2:
        prime = False

    divisor = 2
    while divisor*divisor <= number:
        if number % divisor == 0:
            prime = False
        else:
            prime = True
        divisor += 1

    return prime


def interest_payments(principal_amount, interest_rate, payment):
    """
    -------------------------------------------------------
    Prints a table of monthly interest and payments on a loan.
    Use: interest_payments(principal_amount, interest_rate, payment)
    -------------------------------------------------------
    Parameters:
        principal_amount - original value of a loan (float > 0)
        interest_rate - yearly interest interest_rate as a % (float >= 0)
        payment - the monthly payment (float > 0)
    Returns:
        None
    ------------------------------------------------------
    """

    month = 1
    balance = principal_amount

    print(f"Principal: ${principal_amount: .2f}")
    print(f"Interest Rate: {interest_rate:.2f}%")
    print(f"Monthly payment: ${payment:.2f}")
    print("----------------------------------")
    print("Month   Interest   Payment   Balance")
    print("----------------------------------")

    interest_rate /= 100

    while balance > 0:
        interest = balance * (interest_rate / 12)

        if payment >= balance + interest:
            payment = balance + interest
            balance = 0
        else:
            balance -= payment - interest

        print(f"  {month:<5d}   {interest:8.2f}   {payment:7.2f}   {balance:7.2f}")

        month += 1

    return


def digits_count(number):
    """
    -------------------------------------------------------
    Counts the number of digits in an integer.
    Use: digits = digits_count(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int)
    Returns:
        digits - the number of digits in number (int)
    ------------------------------------------------------
    """
    if number == 0:
        digits = 1
    number = abs(number)
    digits = 0
    while number > 0:
        number //= 10
        digits += 1

    return digits


def sum_factors(number):
    """
    -------------------------------------------------------
    Determines the sum of factors of an integer not including
    the integer itself. An integer's factors are the whole numbers
    that the integer can be evenly divided by.
    Use: total = sum_factors(number)
    -------------------------------------------------------
    Parameters:
        number - a positive integer (int >= 1)
    Returns:
        total - the total of number's factors (int)
    ------------------------------------------------------
    """

    total = 0
    num = 1

    while num < number:
        if number % num == 0:
            total += num
        num += 1
    return total
