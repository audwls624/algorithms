n = int(input())
brackets = list()
for i in range(n):
    bracket = str(input())
    brackets.append(bracket)

def is_bracket_true(bracket_str):
    stack = list()
    for bracket in bracket_str:
        if bracket == '(':
            stack.append(bracket)
        else:
            if not stack:
                return "NO"
            stack.pop()
    if stack:
        return "NO"
    return "YES"
        
for bracket in brackets:
    print(is_bracket_true(bracket))
