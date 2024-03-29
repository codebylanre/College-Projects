from random import randint
import random
import math

def balloons(balloons, children):
    balloons = int(input("Number of balloons: "))
    children = int(input("Number of childrean: "))


    per_child = balloons // children
    left_over = balloons % children

    print(f"Balloons per child: {per_child}")
    print(f"Balloons left over: {left_over}")

def formattedouputlab03n11():

    location1 = "left"
    location2 = "middle"
    location3 = "right"

    print(f"{location1:-<20s}")
    print(f"{location2:-^20s}")
    print(f"{location3:->20s}")

def formattedouputlab03n12():
    first = 100
    second = 34
    third = 933

    total = first + second + third

    # print(f"First: {first:_>6d} ")
    # print(f"Second: {second:_>6d}")
    # print(f"Third: {third:_>6d}")
    # print(f"Total: {total:_>6d}")

    print(f"""
    First:  {first:_>6d}
    Second: {second:_>6d}
    Third:  {third:_>6d}
    Total:  {total:_>6d}
    """)

def functionsdateextractass03n03():
    """
    -------------------------------------------------------
    Extracts the year, month, and day from a date number in the format DDMMYYYY.
    Use: year, month, day = date_extract(date_number)
    -------------------------------------------------------
    Parameters:
        date_number - a date number in the format DDMMYYYY (int)
    Returns:
        year - year portion of date_number (int)
        month - month portion of date_number (int)
        day - day portion of date_number (int)
    ------------------------------------------------------
    """
    date_number = int(input("Enter a date in the format DDMMYYYY: "))    

    day = date_number // 1000000
    month = (date_number % 1000000) // 10000
    year = date_number % 10000
    result = year, month, day
    return result
    # print(f"{year},{month},{day}")

def decisiontargetlab05n04(target, v1, v2):
    """
    -------------------------------------------------------
    Determines closest value of two values to a target value.
    Use: result = closest(target, v1, v2)
    -------------------------------------------------------
    Parameters:
        target - the target value (float)
        v1 - first comparison value (float)
        v2 - second comparison value (float)
    Returns:
        result - one of v1 or v2 that is closest to target,
          v1 is the value chosen if v1 and v2 are an equal
          distance from target (float)
    -------------------------------------------------------
    """
    distance1 = abs(target - (v1))
    distance2 = abs(target - (v2))

    if distance1 <= distance2:
        result = (v1)
    else:
        result = (v2)
    return result

def decisionis_leaplab05n05(year):
    """
    😭
    -------------------------------------------------------
    Determines if a year is a leap year. Every year that is
    exactly divisible by four is a leap year, except for years
    that are exactly divisible by 100, but these centurial years
    are leap years if they are exactly divisible by 400. For
    example, the years 1700, 1800, and 1900 are not leap years,
    but the years 1600 and 2000 are.
    Use: result = is_leap(year)
    -------------------------------------------------------
    Parameters:
        year - a year (int > 0)
    Returns:
        result - True if year is a leap year,
            False otherwise (boolean)
    ------------------------------------------------------
    """

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                result = True
            else:
                result = False
        else:
            result = False
    else:
        result = False
    
    return result 

def decisionfast_foodlab05n15():
    """
    😭
    -------------------------------------------------------
    Food order function.
    Asks user for their order and if they want a combo, and if
    necessary, what is the side order for the combo:
    Prices:
        Burger: $6.00
        Wings: $8.00
        Fries combo: add $1.50
        Salad combo: add $2.00
    Use: price = fast_food()
    -------------------------------------------------------
    Returns:
        price - the price of one meal (float)
    -------------------------------------------------------
    """
    """sample execution
    Order B - burger or W - wings: W
    Make it a combo? (Y/N): Y
    Add F - fries or S - salad: F

    9.50"""
    cost = 0

    order = input("B - burger or W - wings: ")
    if order == "W":
        cost += 8
    elif order == "B":
        cost += 6
    combo = input("Make it a combo? (Y?N): ")
    if combo == "Y":
        which = input("Add F - fries or S - salad: ")
        if which == "F":
            cost += 1.5
        elif which == "S":
            cost += 2.5
    else:
        cost += 0
    result = "{:.2f}".format(cost) #formated it in the function cause i can
    return result
    #refer to the main coursework for a more optimised approach

def decisionlargest_totalass04n03(val1, val2, val3):
    """
    😭
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
    max = 0
    max2 = 0
    if val1 > val2:
        max = val1
    else:
        max2 = val2

    if val3 > val1:
        max = val3
    elif val3 > val2:
        max2 = val3

    result = max2 + max
    return result

def notthusrandomlab05wk6():
    import random
    count0 = 0
    count1 = 1
    for i in range(1000):
        n = random.randint(0, 1)
        if n == 0:
            count0 += 1
        else:
            count1 += 1
    print("Count of 0 is", count0)
    print("Count of 1 is", count1)

def sentinelsfromlab05wk6():


    total = 0
    count = 0

    while True:
        score = int(input("Enter a test score (-1 to exit): "))
        if score == -1:
            break
        total += score
        count += 1

    if count > 0:
        average = total / count
        print(f"Total: {total}")
        print(f"Count: {count}")
        print(f"Average: {average:.2f}")
    else:
        print("No test scores were entered.")

def sentinelsfromlab06wk7():
    score = int(input("Enter a test score (betwenn 0 and 100): "))

    total = 0
    count = 0
    while score != -1:
        total += score
        count += 1
        score = int(
            input("Enter a test score (between 0 and 100, enter -1 to quit): "))

    average = total/count
    print(f"The total is {total}, the count is {count} and average is {average}")

def forloopssum_evenlab06n01(num):
    """
    -------------------------------------------------------
    Sums and returns the total of all even numbers from 2 to num (inclusive).
    Use: total = sum_even(num)
    -------------------------------------------------------
    Parameters:
        num - an integer (int > 0)
    Returns:
        total - sum of all even numbers from 2 to num (int)
    ------------------------------------------------------
    """
    sum = 0
    for i in range(2,num+1,2):
        sum += i
    result = sum
    return result 

def forloopsdraw_trianglelab06n06(height, char):
    """
    😭
    -------------------------------------------------------
    Prints a triangle of height characters using
    the char character.
    Use: draw_triangle(height, char)
    -------------------------------------------------------
    Parameters:
        height - number of characters high (int > 0)
        char - the character to draw with (str, len() == 1)
    Returns:
        None
    ------------------------------------------------------
    """
    a = 4
    return a

def forloopsdraw_arrowlab06n07(width,char):
    """
    -------------------------------------------------------
    Prints a triangle of width characters using
    the char character.
    Use: draw_arrow(width, char)
    -------------------------------------------------------
    Parameters:
        width - number of characters wide (int > 0)
        char - the character to draw with (str, len() == 1)
    Returns:
        None
    ------------------------------------------------------
    """

def forloopsstatisticslab06n15(n):
    """
    😭😭😭😭😭😭
    -------------------------------------------------------
    Asks a user to enter n values, then calculates and returns
    the minimum, maximum, total, and average of those values.
    Use: minimum, maximum, total, average = statistics(n)
    -------------------------------------------------------
    Parameters:
        n - number of values to process (int > 0)
    Returns:
        minimum - smallest of n values (float)
        maximum - largest of n values (float)
        total - total of n values (float)
        average - average of n values (float)
    ------------------------------------------------------
    """
    sum = 0
    # total = int(input("First value: "))
    maximum = minimum = total
    count = 0
    # maximum = int

    total = int(input("First value: "))
    for i in range(n-1):
        count += 1
        total = int(input("Next value: "))
        if total < minimum:
            minimum = total
        if total > maximum:
            maximum = total
        
        sum += total
        
        
        
        
    return sum

def forloopsia_hourslab06n14(ia_count):
    """
    Calculates the total number of hours that IAs (Instructional
    Assistants) work over a 6-week period by asking for the hours
    for each IA per week.
    Use: total_hours = ia_hours(ia_count)
    """
    total_hours = 0

    for week in range(1, 7):
        print("Week", week)
        for ia in range(1, ia_count + 1):
            hours = float(input(f"  Marking hours for IA {ia}: "))
            total_hours += hours

    return total_hours

    # Get the number of IAs from the user
    ia_count = int(input("Enter the number of IAs: "))

    # Calculate the total hours
    total_hours = ia_hours(ia_count)

    # Print the total hours
    print(f"Total hours worked by all IAs: {total_hours:.2f}")
  
def forloopslumberlab06n13_crucialforformattedprinting(b_min, b_max, b_inc, h_min, h_max, h_inc):
    """
    Create a table of the engineering properties of lumber.
    Given the base and height of a piece of lumber in inches,
    different properties of a piece of lumber are calculated.
    """
    print(f"{'Base':>5} x {'Height':<5} {'Cross-Sectional Area':>15} {'Moment of Inertia':>11} {'Section Modulus':>10}")
    print("-" * 49)

    for base in range(b_min, b_max + 1, b_inc):
        for height in range(h_min, h_max + 1, h_inc):
            cross_sectional_area = base * height
            moment_of_inertia = base * height ** 3 / 12
            section_modulus = base * height ** 2 / 6

            print(f"{base:5} x {height:<5} {cross_sectional_area:15.2f} {moment_of_inertia:11.2f} {section_modulus:10.2f}")

def forloopsgiclab06n12(value, years, rate):
    """
    -------------------------------------------------------
    Calculates and prints a table of how much a GIC (Guaranteed
    Income Certificate) is worth over a number of years, and
    returns its final value.
    Use: final_value = gic(value, years, rate)
    -------------------------------------------------------
    Parameters:
        value - GICs initial value (int > 0)
        years - number of years to maturity (int > 0)
        rate - percent increase value per year (float > 0)
    Returns:
        final_value - the final value of the GIC (float)
    ------------------------------------------------------
    """
    print(f"""
        Year          Value $
        ------------------------
            """)
    for years in range(0, years+1):
        print(f"""
        {years:2d}              {value:4,.2f}
        """)
        final_value = value*(1+(rate/100)**years)
        value = value*(1+(rate/100))

    return final_value

def clocksimulate():
    for hours in range(24):
        for minutes in range(60):
            for seconds in range(60):
                print(f"{hours}:{minutes}:{seconds}")

def whilelooptask1advancedlab05wk6(n):
    n = int(input("Enter number of data times: "))
    i = 0
    while i < n:
        sales = float(input('Enter the amount of sales: '))
        comm_rate = float(input('Enter the commission rate (%): '))
        commission = sales*comm_rate / 100
        print(f'The commission is ${commission:,.2f}')
        i = i+1

def forloopsfactorial_ass05n01(number):
    """
    -------------------------------------------------------
    Calculates and returns the factorial of number.
    Use: product = factorial(number)
    -------------------------------------------------------
    Parameters:
        number - number to factorial (int > 0)
    Returns:
        product - number! (int)
    ------------------------------------------------------
    """
    result = 1
    for i in range(1, number+1, 1):
        result *= i
        
    return result
    #start from assignmment 5

def forloopsarrow_rightass05n03(width):
    """
    😭😭😭😭😭
    -------------------------------------------------------
    CPrints an arrow of characters
    Use: arrow_right = arrow_right(width)
    -------------------------------------------------------
    Parameters:
        width - width of characters
    Returns:
        characters
    ------------------------------------------------------
    """
    return width

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
        print(f"  {i:3}", end="")
    print("\n -------------")

    for j in range(start_num, stop_num + 1):
        print(f"{j:2}|", end="")
        for j in range(start_num, stop_num+1):
            print(f"{j *i:4}", end="")
        print()

    return

def forloopsrange_sumass05n05(start, increment, count):
    """
    -------------------------------------------------------
    Uses a for loop to sum values from start by increment.
    Use: total = range_sum(start, increment, count)
    -------------------------------------------------------
    Parameters:
        start - the range start value (int)
        increment - the range increment (int)
        count - the number of values in the range (int)
    Returns:
        total - the sum of the range (int)
    ------------------------------------------------------
    """
    
    total = 0
    for i in range(count):
        total += start
        start += increment
    return total

    print(forloopsrange_sumass05n05(1, 2, 20))

def whileloops_hi_lo_gamelab07n01(high):
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
        count += 1
        guess = int(input("Guess: "))
        if guess > number:
            print("Too high, try again.")
        elif guess < number:
            print("Too low, try again.")
        else:
            print("Congratulations - good guess!")
            break
    print(f"You made {count} guesses.")
    return count

def whileloopsmeal_costlab07n07():
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

    day = 0

    while True:
        day += 1
        print(f"For Day {day}")
        print()
        breakfast = float(input("How much was breakfast? $"))
        b_total += breakfast
        lunch = float(input("How much was lunch? $"))
        l_total += lunch
        supper = float(input("How much was supper? $"))
        s_total += supper
        total = breakfast + lunch + supper

        a_total += total
        print(f"Your total for the day was ${total}")
        print()
        another = input("Were you away for another day (Y/N)? ")
        print()
        if another == "Y":
            continue
        else:
            break
    return b_total, l_total, s_total, a_total
    print(whileloopsmeal_costlab07n07())

def listlab07wk8list():
    
    def max_even_numbers(numbers):
        even = []
        for num in numbers:
            if num % 2 == 0:
                even.append(num)

        return max(even)
    numbers = [1, 2, 3, 4, 57, 35, 26, 36, 2, 32, 234]
    number = max_even_numbers(numbers)
    print(number)

    def lotterynumberlistunderstanding():
        lottery_numbers = []

        # GENERATE NUM
        for num in range(7):
            lottery_numbers.append(random.randint(0, 9))

        # DISPLAY CONTENT
        for value in lottery_numbers:
            print(value, end=" ")

def whileloops_choose_winnerass06n01():
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
    other = 0
    # winning = input("Enter the winning team: ")
    while True:
        winning = input("Enter the winning team: ")

        if winning == "":
            break
        elif winning == "red":
            red += 1
        elif winning == "green":
            green += 1
        else:
            other += 1

        # winning = input("Enter the winning team: ")
    
    return (f"""
The numbers of red is {red}, 
The number of green is {green}, 
The number of other colors is {other}
            """)

def whileloops_is_primeass06n02(number):
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

    divisor = 2
    is_prime = True
    while divisor < number:
        
        if divisor % number == 0:
            is_prime = False

        divisor += 1
    return is_prime

def whileloops_formattedoutput_interest_payments_jsutscanitandreviseit_ass06n03(principal_amount, interest_rate, payment):
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

def whileloops_digits_counts_ass06n04(number):
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
    digits = 0
    while number > 0:
        number //= 10
        digits += 1
    return digits
    #refer to maincode for some optimised moves

def whileloops_sum_factors_ass06n05(number):
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

def randomnumunderstanding():
    def randint():
        # randint(start, stop)
        randomnum = randint(10, 40)
        print(randomnum)
        print()
        for i in range(randomnum):
            print(i)
    def randrange():
        # randrange(start, limit, increment)
        randomnum = randrange(5, 31, 5)
        print(randomnum)
        print()
        for i in range(randomnum):
            print(i)
    def randomm():
        # you can't use a float in a for loop because, think of it with your brain
        # Returns a random floating point number between 0.0 (inclusive) and 1.0 (exclusive).
        randomnum = random()
        print(randomnum)
    def uniform():
        randomnum = uniform(10, 40)
        # uniform(m,n)
        # Returns a random floating point number between m (inclusive) and n (inclusive).
        print(randomnum)
        print()
        for i in range(randomnum): # this line would generate an error
            print(i)

def list_generate_integer_list_lab08n04(n, low, high):
    """
    -------------------------------------------------------
    Generates a list of random integers.
    Requires import: from random import randint
    Use: values = generate_integer_list(n, low, high)
    -------------------------------------------------------
    Parameters:
        n - number of values to generate (int, > 0)
        low - low value range (int)
        high - high value range (int, > low)
    Returns:
        values - a list of random integers (list of int)
    -------------------------------------------------------
    """
    # values = []
    # for i in range(n):
    #     value = randint(low, high)
    #     values.append(value)
    # return values

    values = []
    for i in range(n):
        values.append(randint(low, high))
    return values

def list_sumsoftwolists_lab08n12(source1, source2):
    """
    -------------------------------------------------------
    Calculates sums of elements of two lists. Lists must be the
    same length.
    Use: target = list_sums(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - list of numbers (list of float)
        source2 - list of numbers (list of float)
    Returns:
        target - sums of elements of source1 and source2 (list of float)
    -------------------------------------------------------
    """
    target = []
    if len(source1) != len(source2):
        print("list must be of the same length")
    for i in range(len(source1)):
        result = source1[i] + source2[i]
        target.append(result)
    return target
    # for num in source1 + source2:
    #     result = source1[num] + source2[num]
    #     target.append(result)
    # return target
    print(list_sumsoftwolists_lab08n12([10, 3, 10, 3, 1], [8, 2, 7, 3, 6]))

def list_union_and_intersection_lab08n13(source1, source2):
    """
    -------------------------------------------------------
    Returns a list that is the union of the contents of source1 and source2.
    Every element that appears at least once in either source1 and source2
    must appear once and only once in target.
    Use: target = union(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a list (list of *)
        source2 - a list (list of *)
    Returns:
        target - the union of source1 and source2 (list of *)
    -------------------------------------------------------
    """
    target = []

    for num in (source1 + source2):  
        if num not in target:
                target.append(num)
    return target

    # for union intersection
    # for item in source1:
    #     if item in source2 and item not in target:
    #         target.append(item)
            
    # return target


    print(list_union_and_intersection_lab08n13([10, 3, 10, 3, 1], [8, 2, 7, 3, 6, 10, 32, 99]))

def list_symmetric_difference_lab08n15(source1, source2):
    """
    -------------------------------------------------------
    Returns a list that is the symmetric difference of the contents
    of source1 and source2.
    Only elements that appear in one of source1 and source2, but not both,
    appear once and only once in target.
    Use: target = symmetric_difference(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a list (list of *)
        source2 - a list (list of *)
    Returns:
        target - the symmetric difference of source1 and source2 (list of *)
    -------------------------------------------------------
    """
    target = []
    for num in source1:
        if num not in source2 and num not in target:
            target.append(num)
    for num in source2:
        if num not in source1 and num not in target:
            target.append(num)
    return target
    # for num in (source1 + source2):
    #     if num not in source1 and source2:
    #         target.append(num)
    # return target

    print(list_symmetric_difference_lab08n15([10, 3, 10, 3, 1], [8, 2, 7, 3, 6, 10, 32, 99]))

def list_functionstonote():
    def note():
        word = "Abdulbasit is a good programmer"
        words = word.split()
        print(words[0])
    def time(string):
        words = string.split("/")
        first = words[0]
        second = words[1]
        third = words[2]
        print("day:", first)
        print("month:", second)
        print("year:", third)

        time('20/5/20')

def list_list_all_factors_ass07n01(number):
    """
    -------------------------------------------------------
    Returns a list of factors for a given number.
    use: list = list_all_factors(number)
    -------------------------------------------------------
    Parameters:
        number (int): The integer for which to find the factors.
    Returns:
        A list of factors of the given number, excluding the number itself.
    -------------------------------------------------------
    """
    factors = []
    for num in range(1, number):
        if number % num == 0:
            factors.append(num)   
    return factors

    print(list_list_all_factors_ass07n01(24))

def list_list_indexes_ass07n03(numbers, target_number):
    """
    -------------------------------------------------------
    Finds the indexes of target_number in numbers.
    Use: index_list = list_indexes(numbers, target_number)
    -------------------------------------------------------
    Parameters:
        numbers - list of values (list)
        target_number - value to look for in num_list (*)
    Returns:
        index_list - list of indexes of target_number (list of int)
    -------------------------------------------------------
    """
    index = []
    for i in range(len(numbers)):
        if target_number == numbers[i]:
            index.append(i)
    return index

    print(list_list_indexes_ass07n03([5, 1, 8, 9, 5, 2, 5, 3], 5))

def list_subtract_lists_ass07n04(minuend, subtrahend):
    """
    -------------------------------------------------------
    Alters the contents of minuend so that it does not contain
    any values in subtrahend.
    i.e. the values in the first list that appear in the second list
    are removed from the first list.
    Use: subtract_lists(minuend, subtrahend)
    -------------------------------------------------------
    Parameters:
        minuend - a list of values (list)
        subtrahend - a list of values to not include in difference (list)
    Returns:
        None
    ------------------------------------------------------
    """

    sort = [x for x in minuend if x not in subtrahend]
    minuend.clear()
    minuend.extend(sort)
    return minuend
    ## check main code for a different approach
    # for i in (minuend):
    #     if i in subtrahend:
    #         minuend.remove(i)
    # return minuend

    print(list_subtract_lists_ass07n04([5, 5, 4, 5], [5]))

def list_is_sorted_ass07n05(number):
    """
    -------------------------------------------------------
    Determines whether a list is sorted.
    Use: in_order, index = is_sorted(numbers)
    -------------------------------------------------------
    Parameters:
        numbers - a list of numbers (list)
    Returns:
        in_order - True if numbers is sorted, False otherwise (bool)
        index - index of first value not in order,
            -1 if in_order is True (int)
    ------------------------------------------------------
    """
    
    newlist = [x for x in number]
    newlist. sort()
    if newlist == number:
        result = True
        index = -1
    else:
        result = False
        index = 1
    return result, index

    print(list_is_sorted_ass07n05([3,1,2]))

def strings_validate_code_lab09n04(product_code):
    """
    this made me understand the difference between if and elif
    -------------------------------------------------------
    Parses a given product code and prints whether the various parts are valid.
    A product code has three parts:
        The first three letters describe the product category and must
        all be in upper case.
        The next four digits are the product ID.
        The remaining characters describe the product's qualifiers,
        such as colour, size, etc. and always begins with an uppercase letter.
    Use: category, digits, qualifiers = validate_code(product_code)
    -------------------------------------------------------
    Parameters:
        product_code - a product code (str)
    Returns:
        category - True if three upper-case characters, False otherwise
        digits - True if four digits, False otherwise
        qualifiers - True if starts with 1 upper-case letter, False otherwise
    -------------------------------------------------------
    """
    n = len(product_code)
    digits = qualifier = char = False

    if n>= 3 and product_code[:3].isalpha() and product_code[:3].isupper():
        char = True
    if n>=7 and product_code[3:7].isdigit():
        digits = True
    if n>=8 and product_code[7].isupper():
        qualifier = True
    return char, digits, qualifier

    print(strings_validate_code_lab09n04("BFG"))
    # BFG9000x7

def strings_text_analyze_lab09n10(txt):
    """
    -------------------------------------------------------
    Analyzes txt and returns the number of uppercase letters,
    lowercase letters, digits, and number of whitespaces in txt.
    Use: uppr, lowr, dgts, whtspc = text_analyze(txt)
    -------------------------------------------------------
    Parameters:
        txt - the text to be analyzed (str)
    Returns:
        uppr - number of uppercase letters in txt (int >= 0)
        lowr - number of lowercase letters in txt (int >= 0)
        dgts - number of digits in txt (int >= 0)
        whtspc - number of white spaces in the text (spaces, tabs, linefeeds) (int >= 0)
    ------------------------------------------------------
    """
    uppr = 0
    lowr = 0
    dgts = 0
    whtspc = 0

    for char in txt:
        if char.isupper():
            uppr += 1
        if char.islower():
            lowr += 1
        if char.isdigit():
            dgts += 1
        if char.isspace():
            whtspc += 1
    return uppr, lowr, dgts, whtspc

    print(strings_text_analyze_lab09n10("Python uses whitespace indentation, rather than curly brackets or keywords, to delimit blocks."))

def strings_dsmvwl_lab09n11(string):
    """
    -------------------------------------------------------
    Disemvowels a string. Returns a copy of s with all the vowels
    removed. Y is not treated as a vowel. Preserves case.
    Use: out = dsmvwl(sstring)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        out - string with its vowels removed (str)
    -------------------------------------------------------
    """
    vowel = "IAEIOUaeiou"
    
    new_string = "".join([x for x in string if x not in vowel])
    return new_string
    # for char in string:
    print(strings_dsmvwl_lab09n11("I think your book is an utter piece of garbage."))

def string_comma_period_replacelab09n12(string):
    """
    -------------------------------------------------------
    Replaces all the commas with a period in s.
    Use: out = comma_period_replace(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        out - string with all commas replaced by a period (str)
    ------------------------------------------------------
    """
    for char in string:
        out = string.replace(",",".")
        # if char == ",":
        #     string[char].replace(".")
    return out

    print(string_comma_period_replacelab09n12('Number 1, Number 2, Number 3,'))

def string_str_distance_lab009n14(s1, s2):
    """
    -------------------------------------------------------
    Finds the distance between the s1 and s2. The distance between two
    strings of the same length is the number of positions in the strings
    at which their characters are different. If two strings are not the
    same length, the distance is unknown (-1). If the distance is zero,
    then two strings are equal.
    Use: d = str_distance(s1, s2)
    -------------------------------------------------------
    Parameters:
        s1 - first string (str)
        s2 - second string (str)
    Returns:
        d - the distance between s1 and s2 (int)
    ------------------------------------------------------
    """
    if s1 == "" or s2 == "":
        return 0
    if len(s1) != len(s2):
        return -1
    d = 0
    i = 0
    while i < len(s1):
        if s1[i] != s2[i]:
            d += 1
        i += 1
    result = d
    return result

    print(string_str_distance_lab009n14("North", "South")) 

def string_calculate_lab09n15(expr):
    """
    -----------------------------------------------------------------
    Treats expr as a math expression and evaluates it.
    expr must have the following format:
        operand1 operator operand2
    operators are: +, -, *, /, %
    operands are one-digit integer numbers
    Return None if second operand is zero for division.
    Use: result = calculate(expr)
    -----------------------------------------------------------------
    Parameters:
        expr - an arithmetic expression to be calculated (str)
    Returns:
        result - The result of arithmetic expression (float)
    -----------------------------------------------------------------
    """
    num = int(expr[0])
    sign = (expr[2])
    num1 = int(expr[4])
    if sign == "+":
        result = num + num1
    elif sign == "-":
        result = num - num1
    elif sign == "*":
        result = num * num1
    elif sign == "/":
        if num1 == 0:
            return None  # Division by zero
        result = num / num1
    elif sign == "%":
        if num1 == 0:
            return None  # Division by zero
        result = num % num1
    else:
        return None  # Invalid operator

    return result

    # new = (num + sign + num1)
    # new = "".join([num, sign, num1])
    # woa = int(new)
    # return new
    print(string_calculate_lab09n15('5 + 4'))

def string_spaced_stringass08n01(sentence):
    """
    😭😭
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
    spaced = sentence[0]

    for char in range(1, len(sentence)):
        if sentence[char].isupper():
            spaced += " " + sentence[char].lower()
        else:
            spaced += sentence[char].lower()
    return spaced

    print(string_spaced_stringass08n01("StopAndSmellTheRoses."))

    """ 
    Sure, I'll explain the code step by step:

    1. `def spaced_string(sentence):`
    - This is a function definition. It defines a function named `spaced_string` that takes one parameter called `sentence`.

    2. `spaced = sentence[0]`
    - This initializes a variable `spaced` with the first character of the input `sentence`. This is done to retain the first character as it is.

    3. `for char in range(1, len(sentence)):` 
    - This sets up a loop that iterates over the indices of the characters in the `sentence` starting from the second character (index 1) up to the last character. The `range` function generates a sequence of numbers from 1 to `len(sentence) - 1`.

    4. `if sentence[char].isupper():`
    - This is an `if` statement that checks if the character at the current index (`char`) of the `sentence` is an uppercase letter. The `isupper()` method is used to determine if the character is in uppercase.

    5. `spaced += " " + sentence[char].lower()`
    - If the character is uppercase (as determined by the previous `if` statement), it adds a space followed by the lowercase version of the character to the `spaced` string. This effectively adds a space before each uppercase letter while converting it to lowercase.

    6. `else:`
    - This is the `else` part of the `if` statement, which means the current character is not uppercase.

    7. `spaced += sentence[char].lower()`
    - If the character is not uppercase, it adds the lowercase version of the character directly to the `spaced` string.

    8. `return spaced`
    - This line returns the modified `spaced` string after the loop has finished processing all the characters in the `sentence`.

    9. `print(spaced_string("StopAndSmellTheRoses."))`
    - This line calls the `spaced_string` function with the input `"StopAndSmellTheRoses."`. The function processes the input string and returns the modified string. The result is then printed to the console.

    Overall, the purpose of this code is to take a sentence as input, modify it to insert spaces before each uppercase letter (while converting them to lowercase), and return the modified sentence. The example input `"StopAndSmellTheRoses."` would output `"s top and smell the roses."` after processing.
    """

    """
    Certainly! Let's go through point 2 in more detail:

    2. `spaced = sentence[0]`
    - This line initializes a variable named `spaced` with the first character of the input `sentence`. The purpose of this line is to preserve the first character of the input sentence without any modifications.

    Let's take a look at why this line is important in the context of the code:

    The goal of the code is to convert a sentence in CamelCase (or PascalCase) into a spaced lowercase sentence. In CamelCase, words are combined without spaces, and each word (except the first) begins with an uppercase letter. For example, `"StopAndSmellTheRoses."` is in CamelCase.

    The desired output is `"s top and smell the roses."`, where each word is separated by a space and all letters are in lowercase.

    To achieve this, the code processes each character of the input sentence and checks whether it's an uppercase letter. If it's an uppercase letter, the code inserts a space before it and converts it to lowercase. If it's not an uppercase letter, the code simply adds it to the result string.

    However, the first character of the input sentence should not be processed in the same way as the rest of the characters. It should be preserved exactly as it is. That's why the line `spaced = sentence[0]` initializes the `spaced` variable with the first character of the input sentence. This ensures that the first character remains unchanged, and the subsequent processing inside the loop only modifies the remaining characters.

    In other words, the `spaced` variable acts as a buffer to store the modified sentence, character by character, as the loop processes each character. The first character, which is already in the `spaced` variable, does not undergo any modification.

    After the loop finishes processing all characters in the sentence, the modified and spaced sentence is stored in the `spaced` variable, and it is returned as the output of the function.
    """

def string_pluralized_string_ass09n02(string):
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

def string_commonending_ass09n03(str1, str2):
    """
    😭😭😭
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

    # Initialize the longest common ending
    # suffix = ""

    # # Find the minimum length between the two strings
    # min_length = min(len(str1), len(str2))

    # # Iterate from the end of the strings to the beginning
    # for i in range(1, min_length + 1):
    #     # Check if the characters from the end match
    #     if str1[-i] == str2[-i]:
    #         suffix = str1[-i] + suffix
    #     else:
    #         break  # Stop if characters don't match

    # return suffix

def string_is_isbn_ass09n04(isbn):
    def notethis():
        if isbn.count("-") == 4 and isbn.replace("-","").isdigit() and len(isbn.replace("-", "")) == 5:
            return False
        else:
            return True
        print(string_is_isbn_ass09n04("1----2324"))
    def notethis1():
        space = None
        isbn = isbn.split('-')
        space = "".join([i for i in isbn])

        return space
        print(lies("12-23-32-23-23"))
    """
    one of my fav codes, a lot of magic happening here
    incomplete tho
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
    is_valid = False

    n = len(isbn)
    if all(char.isdigit() or char == '-' for char in isbn):
        if isbn.count("-") == 4 and isbn.replace("-","").isdigit() and len(isbn.replace("-", "")) == 13:
            if isbn[:3] == "978" or isbn[:3] == "979":
                if isbn[-1].isdigit() and not isbn[-2].isdigit():
                    if n == 17:
                        is_valid = True

    return is_valid

            
    print(string_is_isbn_ass09n04('978-3-12148410--0'))
    print(string_is_isbn_ass09n04('978-3-16-148410-0'))

def string_multidimensionalarrayskindofused_isword_chain_ass05n05(words):
    """
    -------------------------------------------------------
    Determines if a list of strings is a word chain. A word chain
    is a list of words in which the last character of a word in
    the list is the same as the first character of the next word
    in the list.
    Use: word_chain = is_word_chain(words)
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

    print(string_isword_chain(['camel', 'leopard', 'dog', 'giraffe', 'elephant']))

def file_notethis():
    # ___WRITING TO FILE___
    def file_fill(destinations_file, destinations):
        # Write the trip locations to the file
        for destination in destinations:
            destinations_file.write(f"{destination}\n")
        return

    # Call the function
    filename = "/Users/abdulbasitolagunju/school/CP104/schoolrevision/src/travelplans.txt"
    output_file = open(filename, "a")
    city_list = ["Paris", "Prague", "London"]
    # file_fill(output_file, city_list)
    output_file.close()


    # ___READING FROM FILE, WHILE LOOP___
    def file_read(travel_file):
        data = []
        line = travel_file.readline()

        while line != " ":
            # print("Contents: ", line)
            data.append(line.strip())
            line = travel_file.readline()
            
        return data

    filename = "/Users/abdulbasitolagunju/school/CP104/schoolrevision/src/travelplans.txt"
    travel_file = open(filename, "r")
    # travel_contents = file_read(travel_file)
    travel_file.close()

    # ___READING FROM FILE, FOR LOOP___
    def file_read(travel_file):
        data = []

        for line in travel_file:
            data.append(line.strip())
        return data

    filename = input("Enter the file name: ")
    travel_file = open(filename, "r")
    travel_contents = file_read(travel_file)
    travel_file.close()

    # ___FIND SPECIFIC CITY FROM FILE
    def has_city(travel_file, city_name):
        # City name not yet found.
        city_found = True
        # Get the first city in the file.
        city = travel_file.readline()

        while city != "" and city.strip() != city_name:
            # Get the next city in the file.
            city = travel_file.readline()

        # See why loop stopped - end of file or city names match?
        if city == "":
            # End of file reached.
            city_found = False
        return city_found

    filename = input("Enter the file name: ")
    city_name = input("Enter the city name to look for: ")
    travel_file = open(filename, "r", encoding="utf-8")
    result = has_city(travel_file, city_name)
    travel_file.close()

def file_customer_record_lab10n01(fh, n):
    """
    😭😭😭
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
    # result = []
    # i = 1
    
    # for line in range(n+1):
    #     word = fh.readline()
    #     if not line:
    #         break
    #     result = word.split(",")
    # return result

    with open("/Users/abdulbasitolagunju/school/CP104/olag6507_l10/src/customers.txt", "r") as f:
        result = file_customer_record_lab10n01(f, 3)
        print(result)
    

    # fh = "/Users/abdulbasitolagunju/school/CP104/schoolrevision/src/customers.txt"
    # n = ["city", "lope"]
    # output = open(fh, "a+")
    # file_customer_record_lab10n01(output, n)

def file_customer_best_lab10n03(fh):
    """
    -------------------------------------------------------
    Find the customer with the largest balance.
    Assumes file is not empty.
    Use: result = customer_best(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
    Returns:
        result - the record with the greatest balance (list)
    -------------------------------------------------------
    """
    result = []
    max_balance = 0
    line = fh.readline()
    while line != "" and line != "\n": # the and statement checks if a line isnt an emtpy string
        records = line.strip().split(',')
        balance = float(records[3])

        if balance > max_balance:
            max_balance = balance
            result = records
            
        line = fh.readline()
    return result 

    with open("/Users/abdulbasitolagunju/school/CP104/olag6507_l10/src/customers.txt", 'r') as f:
        result = file_customer_best_lab10n03(f)
        print(result)

def file_customer_first_lab10n04(fh):
    """
    -------------------------------------------------------
    Find the customer with the earliest sign-up date.
    Assumes file is not empty.
    Use: result = customer_first(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
    Returns:
        result - the record with the earliest sign-in date (list)
    -------------------------------------------------------
    """  
    result = []

    early_date = '9999-99-99'
    line = fh.readline()
    while line != "":
        records = line.strip().split(',')
        sign_date = records[4]
        # datefile = int
        if sign_date < early_date:
            early_date = sign_date
            result = records
        line = fh.readline()
    return result

    with open("/Users/abdulbasitolagunju/school/CP104/olag6507_l10/src/customers.txt", "r") as f:
        result = file_customer_first_lab10n04(f)
        print(result)

def file_number_stats_lab10n06(fh):
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
    smallest = 999999
    largest = 0
    count = 0
    total = 0
    line = fh.readline()
    while line != "":
        records = int(line.strip())
        count += 1
        if records < smallest:
            smallest = records
        if records > largest:
            largest = records
        total += records
        line = fh.readline()
    average = total/count if count > 0 else 0
    return smallest, largest, total, average

    try:
        with open("/Users/abdulbasitolagunju/school/CP104/olag6507_l10/src/numbers.txt", "r") as f:
            result = file_number_stats_lab10n06(f)
            print("smallest: ", result[0])
            print("Largest: ", result[1])
            print("Total: ", result[2])
            print("Average: ", result[3])
    except FileNotFoundError:
        print("file not found")

def file_count_frequency_word_lab10n10(fh, word):
    """
    -------------------------------------------------------
    Counts the number of appearances of word in fh.
    Case is significant - line in file must match word in case.
    Use: count = count_frequency_word(fh, word)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
        word - the word to search for it in fh (str)
    Returns:
        count - the number of appearance of word in fh (int)
    ------------------------------------------------------
    """  
    count = 0
    line = fh.readline()
   
    while line != "":
        get_word = line.strip()
        if get_word == word:
            count += 1
        line = fh.readline()

    return count

    with open("/Users/abdulbasitolagunju/school/CP104/olag6507_l10/src/words.txt", "r") as f:
        word = "Exercise"
        result = file_count_frequency_word_lab10n10(f, word)
        print(result)

def file_find_shortest_lab10n12(fh):
    """
    WAS TOO LAZY TO UNDERSTAND THIS BUT I UNDERSTAND
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
    
    line = fh.readline()
    shortest_words = line.strip()
    shortest_length = len(line)

    while line != "":
        line = line.strip()
        length = len(line)
        if length < shortest_length:
            shortest_length = length
            shortest_words = line
        line = fh.readline()

    return shortest_words

    fh = open("/Users/abdulbasitolagunju/school/CP104/olag6507_l10/src/words.txt", "r")
    result = file_find_shortest_lab10n12(fh)
    print(result)

def file_file_head_ass09n01(file_handle, count):
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

    with open("/Users/abdulbasitolagunju/school/CP104/schoolrevision/src/travelplans.txt", "r") as f:
        result = file_file_head_ass09n01(f, 5)
        print(result)

def file_number_lines_ass09n04(fh_read, fh_write):
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

    fh = open("/Users/abdulbasitolagunju/school/CP104/olag6507_a09/src/wilde.txt", "r")
    fhr = open("/Users/abdulbasitolagunju/school/CP104/olag6507_a09/src/wilde_numbered.txt", "w")
    file_number_lines_ass09n04(fh, fhr)

# NOT DONE 2D LIST
def two_d_generate_matrix_nums(rows, cols, low, high, value_type):
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
            if value_type == "int":
                number = random.randint(low, high)
            else:
                number = random.uniform(low, high)
            row.append(number)
        matrix.append(row)
    return matrix

    print(two_d_matrix_generate_matrix_nums(3, 4, -10 , 10, "int"))

def two_d_generate_matrix_char(rows, cols):
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
        row = []
        for j in range(cols):
            char = chr(random.randint(97, 122))
            row.append(char)
        matrix.append(row)
    return matrix

    print(two_d_generate_matrix_char(3,4))

def table_matrix_number_somefromattedprintingincludedhere(matrix, value_type):
    """
    check this
    -------------------------------------------------------
    Prints the contents of a 2D list in a formatted table.
    Prints float values with 2 decimal points and prints row and
    column headings.
    Use: print_matrix_num(matrix, 'float')
    Use: print_matrix_num(matrix, 'int')
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of values (2D list)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        None.
    -------------------------------------------------------
    """
    # Check if value_type is valid
    if value_type not in ('float', 'int'):
        raise ValueError("Invalid value_type. Use 'float' or 'int'.")

    # Determine the format string based on the value_type
    if value_type == 'float':
        format_string = "{:.2f}"
    else:  # value_type == 'int'
        format_string = "{}"

    # Determine the width of the columns based on the maximum value length
    max_value_length = max(len(format_string.format(value)) for row in matrix for value in row)

    # Print column headings
    print("Row  |", end="")
    for col in range(len(matrix[0])):
        print(f" Col {col} |", end="")
    print("\n" + "-" * (max_value_length + 10 * (len(matrix[0]) + 1)))

    # Print the matrix values
    for row_idx, row in enumerate(matrix):
        print(f"Row {row_idx} |", end="")
        for value in row:
            print(f" {format_string.format(value)} |", end="")
        print()

    matrix = two_d_generate_matrix_nums(3, 4, -10, 10, "float")
    print(table_matrix_number_somefromattedprintingincludedhere(matrix, "float"))

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
    # using a for loop which is more memory efficient
    # smallest = largest = total = 0
    # num_elements = 0
    # for row in matrix:
    # for value in row:
    #     if num_elements == 0 or value < smallest:
    #         smallest = value
    #     if num_elements == 0 or value > largest:
    #         largest = value
    #     total += value
    #     num_elements += 1

    item = [i for sublist in matrix for i in sublist]
    smallest = min(item)
    largest = max(item)
    total = sum(item)
    average = total / len(item)
    return smallest, largest, total, average
    print(matrix_stats([[2, 0, -1, 1], [10, 4, -5, 9], [-6, 3, 6, 0]]))

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
    # using for loops
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            #multiply each element by sum
            matrix[i][j] *= num
    return
    print(matrix_scalar_multiply([[-6, -3, -7], [-4, 5, -10]], 5))

    # Using lists
    # Done by me 😌 but for loop works smarter
    item = [i * 5 for sublist in matrix for i in sublist]
    return item
    print(matrix_scalar_multiply([[-6, -3, -7], [-4, 5, -10]], 5))

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

    item1 = [i for sublist in matrix1 for i in sublist]
    item2 = [i for sublist in matrix2 for i in sublist]
    if item1 == item2:
        equal = True
    else:
        equal = False
    return equal
    print(matrix_equal([['c', 'a', 't'], ['d', 'o', 'g'], ['b', 'i', 'g']], [['c', 'a', 't'], ['d', 'o', 'g'], ['b', 'i', 'g']]))
    """
    THIS IS A VERY GOOD CODE BUT YOU SHOULD ALSO CHECK 
    THE CODE FROM LAB CAUSE IT USES TWO DIFFERENT APPRAOCHES 
    THAT WORKS JUST SMART
    """

def midterm_count_evens(n):
    """
    -------------------------------------------------------------------------
    Generates n random integers and checks each integer whether it is even.
    Use: number_of_evens = count_evens (n)
    -------------------------------------------------------------------------
    Parameters:
    Returns:
    n - number of random integers to be generated (int > 0)
    Returns:
        number_of_evens - count of the even numbers (int)
    -------------------------------------------------------------------------
    """
    number_evens = 0
    for i in range(n):
        gen = random.randint(1,100)
        if gen % 2 == 0:
            number_evens += 1
    return number_evens

    print(midterm_count_evens(40))

# FIRST SEMESTER EXAM
def finalexam_closest_number(values, target):
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
    closest = 0
    if len(values) == 0:
        closest = 0
    else:
        closest = values[0]
        for value in values:
            difference = abs(target - value)
            if difference < abs(target - closest):
                closest = value
    return closest

    print(finalexam_closest_number([1, 2, 3, 6, 4, 5], 7))

def finalexam_prime_stats(numbers):
    """
    -------------------------------------------------------
    Finds the prime numbers from a list of numbers, and calculates the count, maximum, minimum, and average of those prime numbers.
    A prime number is a positive integer greater than 1 that has no positive integer divisors other than 1 and itself. 
    To find whether a number is prime, you may run a loop from 2 to the square root of the number (inclusive) 
    and check if any integer in the loop divides that number. 
    Use: primes, count, maximum, minimum, average = prime_stats(numbers)
    -------------------------------------------------------
    Parameters:
        numbers - a list of numbers containing both prime and composite numbers (list of int)
    Returns:
        primes - all primes in the list
        count - number of primes in the list
        maximum - the maximum prime in the list
        minimum - the minimum prime in the list
        average - average of primes in the list
    -------------------------------------------------------
    """
    primes = []
    


    for value in numbers:
        prime = True
        if value <= 1:
            prime = False
        else:
            for num in range(2, int(math.sqrt(value))+1):
                if value % num == 0:
                    prime = False
                    break
        if prime:
            primes.append(value)

    count = len(primes)
    total = sum(primes)
    maximum = max(primes)
    minimum = min(primes)
    average = total/count

    return f"{primes}, {count}, {maximum}, {minimum}, {average:.2f}"

    print(finalexam_prime_stats([87, 34, 76, 59, 22, 93, 47, 12, 85, 67]))

def finalexam_alternate_case(string):
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
    for index, letter in enumerate(string):
        if index % 2 == 0:
            alternating += letter.upper()
        else:
            alternating += letter.lower()
    else: 
        alternating += letter
    return alternating

    print(finalexam_alternate_case("THIS IS THE 3RD SENTENCE"))

def file_split(f_in, f_word, f_words):
    """
    -------------------------------------------------------
    Copies the contents of f_in to f_word and f_words depending
    on the contents of f_in:
        Lines containing a single word are copied to f_word.
        Lines containing more than one word are copied to f_words.
        Empty lines are ignored.
    Use: file_split(f_in, f_word, f_words)
    -------------------------------------------------------
    Parameters:
        f_in - source file (file handle - already open for reading)
        f_word - file to contain lines with single words from f_in (file handle
            - already open for writing)
        f_words - file to contain lines with multiple words from f_in
            (file handle - already open for writing)
    Returns:
        None
    -------------------------------------------------------
    """
    line = f_in.readline()

    for line in f_in:
        if len(line.strip()) > 0:
            if len(line.split()) == 1:
                f_word.write(line)
            else:
                f_words.write(line)
    

    with open("/Users/abdulbasitolagunju/school/CP104/schoolrevision/src/source.txt", "r") as f_in:
        with open("/Users/abdulbasitolagunju/school/CP104/schoolrevision/src/word.txt", "w") as f_word:
            with open("/Users/abdulbasitolagunju/school/CP104/schoolrevision/src/words.txt", "w") as f_words:     
                file_split(f_in, f_word, f_words)

