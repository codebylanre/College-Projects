"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Olagunju Abdulbasit
ID:     169076507
Email:  olag6507@laurier.ca
__updated__ = "Oct 8, 2023"
------------------------------------------------------------------------
"""
from ArrayStack import ArrayStack

def is_matched_html(filename):
    """"Return True if all delimiters are properly matched otherwise false"""
    S = ArrayStack()
    tags = ["<name>", "<body>", "<center>", "<h1>", "<p>", "<ol>", "<li>"]
    
    with open(filename, "r") as fh:
        content = fh.read()

        for line in content.splitline:
            # Extract individual
            if line in lefty:
                S.push(line)
            elif line in righty:
                if S.isEmpty():
                    return False
                if lefty.index(line) != righty.index(line):
                    return False
        return S.isEmpty()
     

# Test code starts from here 

print(is_matched_html("Assignment1.txt"))