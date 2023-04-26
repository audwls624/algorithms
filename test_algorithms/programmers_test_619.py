def solution(b):
    for c in range(b, 500001):
        a = (c**2 - b**2)**0.5
        if int(a) == a and a <= b:
            return c
    return -1