'''
Created on Dec. 1, 2023

@author: Abdulbasit
'''


from HashTable import HashTable





def testing_multiplication_method():
    """a new add method was created 
    to implement the multiplication hash method"""

    hashT = HashTable(20)
    hashT.add_multiplicationhash("good","eggs")
    hashT.add_multiplicationhash("better","ham")
    hashT.add_multiplicationhash("ad","spam")
    hashT.add_multiplicationhash("ga","do not collide")
    #hashT.add("good","cake")
    
    
    hashT.printAll()



def testing_MidSquaremethod():
    """a new add method was created 
    to implement the MidSquare hash method"""

    hashT = HashTable(20)
    hashT.add_midSqurehash("good","eggs")
    hashT.add_midSqurehash("better","ham")
    hashT.add_midSqurehash("ad","spam")
    hashT.add_midSqurehash("ga","do not collide")
    #hashT.add("good","cake")
    
    
    hashT.printAll()



def main():
    print()
    testing_multiplication_method()
    print()
    testing_MidSquaremethod()
    print()


main()