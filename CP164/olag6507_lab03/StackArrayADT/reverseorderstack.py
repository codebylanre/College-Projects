'''
Created on Sep 27, 2023

@author: abdulbasitolagunju
'''

#THIS WAS THE CODE CORRRECTION

from ArrayStack import ArrayStack

def reversedstack():
    s1 = ArrayStack()
    
    with open("inputs.txt", 'r') as file:
        content = file.read()
        
        for char in content:
            s1.push(char)
            
    with open('outputs.txt', 'w') as out:
        for i in range(len(s1)):
            out.write(s1.pop())
                    
if __name__ == "__main__":                
    reversedstack()