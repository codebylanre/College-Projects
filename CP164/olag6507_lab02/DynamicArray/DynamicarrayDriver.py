'''
Created on Sep. 20, 2023

@author: 12265
'''
from DynamicArray import DynamicArray

Student_list = DynamicArray()

for x in range(5):
    print()            # mmy
    Student_list.append("Student"+str(x))
    print(Student_list[x])
    print("number of items in Array", len(Student_list))
    print("Total capacity of Array",Student_list._capacity)
    


print("___"*15)
print("Before insertion",Student_list[2])
Student_list.insert(2,"Zara")

print("After insertion",Student_list[2])
# Student_list.remove("Zara")
print(Student_list[2])