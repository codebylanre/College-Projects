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


class Tollbooth:
    def __init__(self):
        self.total_cars = 0
        self.total_amount = 0
          
    def payingCar(self):
        self.total_cars += 1
        self.total_amount += 0.5
    
    def nopayCar(self):
        self.total_cars += 1
        
    def __str__(self):
        return f"The total number of cars is: {self.total_cars}\nThe total amount paid is: $ {self.total_amount}"
        

        