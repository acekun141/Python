"""
Use a stack to check whether or not a string has balanced usage of parenthesis

Exaples:
    (), {}(), {{()}} <- Balanced.
    {}{{{{}}(()()))))) <- Not balanced
"""

from stack import Stack


def is_paren_balanced(paren_string):
    s = Stack()
    is_balanced = True
    index = 0
    DATA = {"{":"}", "(":")", "[":"]"}

    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        if paren in "([{":
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
                break
            top = s.pop()
            if DATA[top] != paren:
                is_balanced = False
        index += 1
    
    if s.is_empty() and is_balanced:
        return True
    else:
        return False
