# 풀이 미완료
def solution(n, lost, reserve):
    result = [0 for _ in range(n)]
    for i in reserve:
        result[i-1] += 2
    
    for j in lost:
        front = j - 2
        back = j
        if 0 <= front < n and result[front] > 1 and result[j - 1] == 0:
            result[front] -= 1
            result[j - 1] += 1
            
        if 0 <= back < n and result[back] > 1 and result[j - 1] == 0:
            result[back] -= 1
            result[j - 1] += 1 
        
    return sum(result)

print(solution(5, [2,4], [1,3,5]))