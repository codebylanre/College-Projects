'''
Created on Sep 27, 2023

@author: abdulbasitolagunju
'''
from ArrayStack import ArrayStack


def print_first_last_stack() :
    first= ArrayStack() #declaring first stack
    last= ArrayStack()  #declare second stack

    first.push("Zara")
    first.push("Pranay") 
    first.push("Yusuf")
    first.push( "Ying")


    last.push("Hamid")
    last.push("Wadhwa")
    last.push("Iqbal")
    last.push("Zeng")

    while not first.isEmpty():
        namestr = first.pop()+ " " + last.pop() 
        print(namestr)



if __name__ == "__main__":
    print_first_last_stack()