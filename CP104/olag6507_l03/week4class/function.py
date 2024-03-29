"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Olagunju Abdulbasit
ID:      169076507
Email:   olag6507@mylaurier.ca
__updated__ = "2023-05-31"
-------------------------------------------------------
"""


def get_hourly_rate():
    rate = float(input("Enter hourly rate: "))
    return rate


def get_number_hours():
    hours = float(input("Enter number of hours: "))
    return hours


def calculate_net_salary(rate, hours):
    salary = rate*hours
    return salary


def main():
    rate = get_hourly_rate()
    hours = get_number_hours()
    salary = calculate_net_salary(rate, hours)
    print(salary)


main()
