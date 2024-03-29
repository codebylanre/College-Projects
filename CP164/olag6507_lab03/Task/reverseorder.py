'''
Created on Sep 27, 2023

@author: abdulbasitolagunju
'''

def reverseorder(fileread, filecopy):
    newlist = []                        # Creates am empty list
    
    
    for line in fileread:          # read lines from the filesthat contains the word
    
        words = line.split()
        reversed_line = ' '.join(word[::-1] for word in words)
        
        # read lines from the read file and copy them to the empty list
        newlist.append(reversed_line)
       
       
       # Reverses the order of the list with the Reverse function
    newlist.reverse()
  


    
    
    # Writes from the fileread to the filecopy 
    with open(filecopy, "w") as fh:
        for line in newlist:
            fh.write(line + '\n')
            

with open("input.txt", 'r') as fileread:
    reverseorder(fileread, "ouput.txt")
    
