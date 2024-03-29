"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Olagunju Abdulbasit
ID:     169076507
Email:  olag6507@laurier.ca
__updated__ = "Oct 7, 2023"
------------------------------------------------------------------------
"""

from ArrayStack import ArrayStack

def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = ArrayStack()
    postfix = []
    tokens = expression.split()

    for token in tokens:
        if token.isnumeric():
            postfix.append(token)
        elif token in "+-*/^":
            while (not stack.isEmpty() and stack.peek() in "+-*/^" and
                   precedence[token] <= precedence[stack.peek()]):
                postfix.append(stack.pop())
            stack.push(token)
        elif token == "(":
            stack.push(token)
        elif token == ")":
            while not stack.isEmpty() and stack.peek() != "(":
                postfix.append(stack.pop())
            if not stack.isEmpty() and stack.peek() == "(":
                stack.pop()

    while not stack.isEmpty():
        postfix.append(stack.pop())

    return " ".join(postfix)

def evaluate_postfix(expression):
    stack = ArrayStack()
    tokens = expression.split()

    for token in tokens:
        if token.isnumeric():
            stack.push(int(token))
        elif token in "+-*/^":
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == "+":
                stack.push(operand1 + operand2)
            elif token == "-":
                stack.push(operand1 - operand2)
            elif token == "*":
                stack.push(operand1 * operand2)
            elif token == "/":
                stack.push(operand1 / operand2)
            elif token == "^":
                stack.push(operand1 ** operand2)

    return stack.pop()

if __name__ == "__main__":
    infix_expression = input("Enter an infix expression: ")
    postfix_expression = infix_to_postfix(infix_expression)
    result = evaluate_postfix(postfix_expression)
    print("Result:", result)
