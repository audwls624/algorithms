def solution(v):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    n = len(v)
    num = []
    count = 0
    result = 0

    def DFS(x, y):
        if x < 0 or x >= len(v) or y < 0 or y >= len(v[0]):
            return False
        
        if v[x][y] == 1:
            nonlocal count
            count += 1
            v[x][y] = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx >= 0 and nx < n and ny >= 0 and ny < n:
                    DFS(nx, ny)
            return True
        return False
    


    for i in range(len(v)):
        for j in range(len(v[0])):
            if DFS(i, j):
                num.append(count)
                result += 1
                count = 0

    return [len(num), max(num)]

v = [[1,1,0,1,1],[0,1,1,0,0],[0,0,0,0,0], [1,1,0,1,1], [1,0,1,1,1], [1,0,1,1,1]]
print(solution(v))