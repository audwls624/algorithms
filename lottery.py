log = dict()
n = 0

lottery = [[1, 0], [2, 0], [3, 0]]

for i in lottery:
    if i[0] in log.keys():
        log[i[0]] += i[1]
    else:
        log[i[0]] = i[1]
arr = [key for key, value in log.items() if value == 0]
for key in arr:
    del(log[key])
for i in log.keys():
    for j in lottery:
        if i == j[0] and j[1] == 0:
            n += 1
        elif i == j[0] and j[1] == 1:
            n += 1
            break
        else:
            continue
print(log)
print(n/len(log.keys()))
print(n)
