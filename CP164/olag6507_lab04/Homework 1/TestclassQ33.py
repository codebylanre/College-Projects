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

def infix_to_postfix(infix_expression):
    operator_precedence = {
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2,
    }

    stack = ArrayStack()
    postfix_expression = []

    def pop_higher_precedence_operators(token):
        while not stack.isEmpty() and operator_precedence.get(stack.peek(), 0) >= operator_precedence.get(token, 0):
            postfix_expression.append(stack.pop())

    for token in infix_expression.split():
        if token in operator_precedence:
            pop_higher_precedence_operators(token)
            stack.push(token)
        elif token == "(":
            stack.push(token)
        elif token == ")":
            while not stack.isEmpty() and stack.peek() != "(":
                postfix_expression.append(stack.pop())
            if not stack.isEmpty() and stack.peek() == "(":
                stack.pop()
            else:
                raise ValueError("Unbalanced parentheses in the expression.")
        else:
            postfix_expression.append(token)

    while not stack.isEmpty():
        if stack.peek() == "(":
            raise ValueError("Unbalanced parentheses in the expression.")
        postfix_expression.append(stack.pop())

    return " ".join(postfix_expression)

def evaluate_postfix_expression(postfix_expression, variables):
    operator_precedence = {
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2,
    }

    stack = ArrayStack()

    for token in postfix_expression.split():
        if token in operator_precedence:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == "+":
                stack.push(operand1 + operand2)
            elif token == "-":
                stack.push(operand1 - operand2)
            elif token == "*":
                stack.push(operand1 * operand2)
            elif token == "/":
                if operand2 == 0:
                    raise ValueError("Division by zero.")
                stack.push(operand1 / operand2)
        elif token in variables:
            stack.push(variables[token])
        else:
            stack.push(float(token))

    if len(stack) != 1:
        raise ValueError("Invalid postfix expression.")
    
    return stack.pop()

def main():
    infix_expression = input("Enter an infix expression: ")
    variables = {}

    try:
        postfix_expression = infix_to_postfix(infix_expression)
        result = evaluate_postfix_expression(postfix_expression, variables)
        print("Result:", result)
    except ValueError as e:
        print("Error:", str(e))

if __name__ == "__main__":
    main()
