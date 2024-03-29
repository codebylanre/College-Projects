'''
Testing class Student
'''
from Student import Student

s1 = Student("123456789", "Hamid", "Zara", "F", "1962-10-25")
s2 = Student("879654321", "Wick", "John", "M", "1984-11-22")


if s1 < s2:
    print("{} {} comes first".format(s1.forename, s1.surname))
elif s2 < s1:
    print("{} {} comes first".format(s2.forename, s2.surname))
else:
    print("The students are the same")
    
print() 
print(s1)


