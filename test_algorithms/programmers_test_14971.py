def solution(number: str) -> int:
    count: int = 0
    ex = set()
    for i in range(len(number)):
        if i in ex:
            continue
        if number[i] == "0":
            count += 1
            continue

        if i < len(number) - 1 and int(number[i+1]) == int(number[i]) + 1:
            count += 1
            ex.add(i+1)
        else:
            count += 2
    return count

print(solution("12156"))
print(solution("321"))
print(solution("1234567"))
print(solution("100"))