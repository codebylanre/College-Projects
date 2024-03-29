"""
Defining Vehicle function
"""

class Vehicle:
    def __init__(self, brand, model, gas_tank_size):
        self.brand = brand
        self.model = model 
        self.gas_tank_size = gas_tank_size
        self.fuel_level = 0

    def add_fuel(self,n):
        self.fuel_level += n

    def drive(self):
        return f"{self.model} is driving"

    def display_vehicle(self):
        return f"{self.brand} {self.model} {self.gas_tank_size} {self.fuel_level} "



# my_car = Vehicle("Toyota", "Camry", 20)
# # my_car.add_fuel(50)
# print(my_car.drive())