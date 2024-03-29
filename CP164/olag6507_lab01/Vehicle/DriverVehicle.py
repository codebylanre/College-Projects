"""
Prof's testing
"""

from Vehicle import Vehicle

def test():
    v1=Vehicle("Honda","CR-V",30) #instantiating/creating an object
    v2=Vehicle("Toyota","Camry",30)
    
    print(v1.display_vehicle())
    v1.add_fuel(20)
    print(v1.display_vehicle())
    print(v2.display_vehicle())
    

if __name__=="__main__":
    test()
    
    
    