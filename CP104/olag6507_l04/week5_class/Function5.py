"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Olagunju Abdulbasit
ID:      169076507
Email:   olag6507@mylaurier.ca
__updated__ = "2023-06-07"
-------------------------------------------------------
"""


def program_for_paint_company():
    square_feet = float(
        input("Enter the square feet of wall space to be painted:"))
    paint_per_gallon = float(input("Enter the price of the paint per gallon:"))

    number_of_gallon = square_feet/112
    hours_of_labor = number_of_gallon * 8
    labor_charges = 35 * hours_of_labor
    cost_of_paint = paint_per_gallon * number_of_gallon
    total_cost = labor_charges + cost_of_paint

    print(f"The number of gallons of paint required is:", number_of_gallon)
    print(f"The hours of labor required is:", hours_of_labor)
    print(f"The cost of the paint is:", cost_of_paint)
    print(f"The total cost is:", total_cost)


program_for_paint_company()
