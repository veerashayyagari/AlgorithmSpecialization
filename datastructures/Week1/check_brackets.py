# python3

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

def CheckBrackets(text):
    opening_brackets_stack = []
    
    for i,next in enumerate(text):
        if next == '[' or next == '(' or next == '{':
            b = Bracket(next,i+1)
            opening_brackets_stack.append(b)
        elif next == ']' or next == ')' or next == '}':
            if len(opening_brackets_stack) > 0:
                b1 = opening_brackets_stack.pop()
                if b1.Match(next) == False:
                    return i+1
            else:
                return i+1

    if len(opening_brackets_stack) == 0:
        return "Success"
    else:
        b1 = opening_brackets_stack.pop()
        return b1.position

if __name__ == "__main__":
    text = sys.stdin.read()

    print(CheckBrackets(text))


