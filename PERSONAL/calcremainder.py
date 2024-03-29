number = int(input("Enter number: "))

divisor = int(input("Input divisor: "))

division = number//divisor 
remainder = number % divisor

print(f"The result of the division is {division}")
while remainder != 0:
    print(f"With remainder of: {remainder}")
    break