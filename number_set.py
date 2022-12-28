def solution(X, Y):
    ans_list = list()
    x_list, y_list = [0 for _ in range(10)], [0 for _ in range(10)]
    
    for i in X:
        x_list[int(i)] += 1
        
    for j in Y:
        y_list[int(j)] += 1
    
    for idx in range(10):
        if x_list[idx] == 0 or y_list[idx] == 0:
            ans_list.append("")
            continue
        ans_list.append(str(idx) * min(x_list[idx], y_list[idx]))
    
    if all(ans_list):
        return "-1"
    return "".join(sorted(ans_list, reverse=True))
        
