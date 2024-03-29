"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Olagunju Abdulbasit
ID:      169076507
Email:   olag6507@mylaurier.ca
__updated__ = "2023-07-02"
-------------------------------------------------------
"""
import math


# def prime_numbers_stats(numbers):
#     count = 0
#     total = 0
#     maximum = 0
#     minimum = 0
#     for num in numbers:
#         if num < 2:
#             print("Number can not be less than 2")
#             break
#             for i in range(2, int(math.sqrt(num))+1):
#                 if num % i == 0:
#                     num == True
#                 else:
#                     num == False
#             while num == True:
#                 total += num
#                 count += 1
#                 maximum = minimum = num
#                 if num > maximum:
#                     maximum = num
#                 elif num < minimum:
#                     minimum = num
#
#     # average = total/count
#
#     return count, maximum, minimum
#
#
#
# prime_numbers_stats(numbers)
# print("Count of prime numbers:", count)
# print("Maximum prime number:", maximum)
# print("Minimum prime number:", minimum)
# print("Average of prime numbers:", average)


import math


def prime_number_stats(numbers):
    count = 0
    maximum = None
    minimum = None
    total = 0

    for num in numbers:
        if num >= 2:
            is_prime = True
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    is_prime = False
                    break

            if is_prime:
                count += 1
                total += num
                if maximum is None or num > maximum:
                    maximum = num
                if minimum is None or num < minimum:
                    minimum = num

    average = total / count if count > 0 else None
    return count, maximum, minimum, average


# Example usage
numbers = [2, 7, 15, 23, 12, 31, 9, 17]
count, maximum, minimum, average = prime_number_stats(numbers)

print("Count of prime numbers:", count)
print("Maximum prime number:", maximum)
print("Minimum prime number:", minimum)
print("Average of prime numbers:", average)
