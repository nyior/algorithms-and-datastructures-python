"""
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
    determine if the input string is valid.

    An input string is valid if:
        - Open brackets must be closed by the same type of brackets.
        - Open brackets must be closed in the correct order.
"""

def is_valid_string(s: str) -> bool:
    stack = []

    for elem in s:
        if elem == "(" or elem =="[" or elem == "{":
             stack.append(elem)
                
        elif stack: 
            last = stack.pop()
                
            if elem == ')' and last != '(':
                return False

            if elem == '}' and last != '{':
                return False

            if elem == ']' and last != '[':
                return False
                
            else:
                return False
                
    return len(stack) == 0
        