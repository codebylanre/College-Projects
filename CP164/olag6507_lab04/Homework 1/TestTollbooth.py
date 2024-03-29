"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Olagunju Abdulbasit
ID:     169076507
Email:  olag6507@laurier.ca
__updated__ = "Oct 7, 2023"
------------------------------------------------------------------------
"""

from Tollbooth import Tollbooth

def Testtollbooth():
    car = Tollbooth()
    
    print("Options")
    print("1. Paying Cars")
    print("2. Non-Paying Cars")
    print("3. Print total")
    print("4. Quit")
    while True:
        try:
            enter = int(input("Enter a number from the list: "))
            if enter == 1:
                car.payingCar()
            elif enter == 2:
                car.nopayCar()
            elif enter == 3:
                print(car)
                break
            else: 
                break
        except:
            print("Please enter a number from the list")
            break
    
if __name__ == "__main__":
    Testtollbooth()
    
