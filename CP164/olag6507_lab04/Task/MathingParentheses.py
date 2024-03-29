from ArrayStack import ArrayStack

def is_matched(expr):
    '''Return True if all delimiters are properly matched; False otherwise.'''
    lefty = '({['  # opening delimiters
    righty = ')}]'  # respective closing delimiters
    S = ArrayStack()

    for c in expr:
        if c in lefty:
            S.push(c)  # push left delimiter
        elif c in righty:
            if S.is_empty():
                return False  # nothing to match
            if righty.index(c) != lefty.index(S.pop()):
                return False  # mismatched

    return S.is_empty()  # were all symbols matched?


