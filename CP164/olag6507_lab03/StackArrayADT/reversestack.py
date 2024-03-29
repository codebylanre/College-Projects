'''
Created on Sep 28, 2023

@author: abdulbasitolagunju
'''

from ArrayStack import ArrayStack




def reversedstack():
    s1 = ArrayStack()
    with open("newinput.txt", "r") as source:

        source_content = source.read()
        for line in source_content:
            s1.push(line)
    
    with open("newoutput.txt", 'w') as out:
        for char in range(len(s1)):
            out.write(s1.pop())
            
            

if __name__ == "__main__":
    reversedstack()