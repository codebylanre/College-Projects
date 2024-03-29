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
from Employee import Employee


def Testingemployee():
    # List of Employee object for testing
    employees = [
    Employee("Abdul", "Basit", "iamabdulbasit@business.com", 50000,  "IT"),
    Employee("Joe", "Lanre", "lanre@business.com", 7000, "Marketing"),
    Employee("Steph", "Smith", "steph@business.com", 60000, "Finance"),
    Employee("Amanda", "Joe", "Amandajoe@business.com", 50000, "IT")
    ]
    
    # Test magic method __str__
    for i, person in enumerate(employees):  # I used enumerate here cause I'm personally trying to work on my usage of it and get familiar with it
        
        print("Employee:",i+1, "\n" + str(person) + "\n")
        
    # Total employee value
    print(f"Total employee: {Employee.total_employee}")
    
    # Test magic method __eq__
    print("testing Equal salary with Employee1 and 4")
    print(employees[0] == employees[3])

if __name__ == "__main__":
    Testingemployee()


