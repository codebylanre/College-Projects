'''
Created on Sep 28, 2023

@author: abdulbasitolagunju
'''

from ArrayStack import ArrayStack

s1 = ArrayStack()
def reversedstack():
    # Working on the reading file
    with open("hi.txt", 'r') as file:
        file_content = file.read()
        for line in file_content:
            s1.push(line)
    
    # OUTPUT FILES STARTS HERE
    with open("outputhere.txt", 'w') as out:
        for i in range(len(s1)):
            out.write(s1.pop())
        
        
        
        
        
        
        
        
if __name__ == "__main__":
    reversedstack()