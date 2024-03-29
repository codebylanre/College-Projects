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
    """Return True if all HTML tags are properly matched; otherwise, return False."""
    S = ArrayStack()
    
    #list of valid HTML tags
    valid_tags = ["<name>", "<body>", "<center>", "<h1>", "<p>", "<ol>", "<li>"]

    with open(filename, "r") as fh:
        content = fh.read()

        for line in content.splitlines():
            
            # Extract individual words (tags) from the line
            tags = line.split()

            for tag in tags:
                
                # Check if the tag is a valid opening tag
                if tag.startswith("<") and not tag.startswith("</"):
                    S.push(tag)
                    
                # Check if the tag is a valid closing tag
                elif tag.startswith("</"):
                    if S.isEmpty():
                        return False
                    tag_name = tag[2:-1]
                    if S.pop() != f"<{tag_name}>":
                        return False

        # After processing the content, the stack should be empty if all tags are properly matched
        return S.isEmpty()


print(is_matched_html("Assignment1.txt"))