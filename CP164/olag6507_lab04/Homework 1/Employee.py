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
import random


class Employee:
    total_employee = 0
    
    def __init__(self, first_name, last_name, email, salary, department):
        self.employee_id = random.randint(1000,1999)
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.salary = salary
        self.department = department
        Employee.total_employee += 1
            
        
    def display_employee(self):
        return f"Total Employee: {self.total_employee}"
    
    def __str__(self):
        return f"first name: {self.first_name}\nLast name: {self.last_name}\nE-mail: {self.email}\nID: {self.employee_id}\nDepartment: {self.department}"
        
        
    def __eq__(self, other):
        result = {self.salary} == {other.salary}
        return f"Equal salary?: {result}"