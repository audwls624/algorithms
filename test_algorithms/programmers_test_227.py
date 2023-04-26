def solution(n):
    if n <= 9:
        return n

    digits = 1
    while n > 9 * 10 ** (digits - 1) * digits:
        n -= 9 * 10 ** (digits - 1) * digits
        digits += 1

    num = 10 ** (digits - 1) + (n - 1) // digits
    return int(str(num)[(n - 1) % digits])