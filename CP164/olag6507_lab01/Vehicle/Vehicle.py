'''
Created on Sep. 13, 2023

@author: Zara
'''

class Vehicle:
    def __init__(self,brand,model,gas_tank_size):
        self.brand=brand
        self.model=model
        self.gas_tank_size=gas_tank_size
        self.fuel_level=0
        
    def add_fuel(self,n):
        self.fuel_level+=n
        
    def drive(self):
        s=""
        s+=self.model+"is driving"
        print(s)
    
    def display_vehicle(self):
        return f"{self.brand},{self.model},{self.gas_tank_size},{self.fuel_level}"