def solution(maps):
    import sys
    sys.setrecursionlimit(int(1e9))
    answer = []
    islands = [list(map) for map in maps]
    max_days = 0
    count = 0
        
    def DFS(x, y):
        nonlocal max_days
        if x < 0 or y < 0 or x >= len(islands) or y >= len(islands[0]):
            return False
        
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        if islands[x][y] != 'X':
            max_days += int(islands[x][y])
            islands[x][y] = 'X'
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                DFS(nx, ny)
            return True
    
    for i in range(len(islands)):
        for j in range(len(islands[0])):
            if islands[i][j] != 'X':
                DFS(i, j)
                answer.append(max_days)
                max_days = 0
    answer.sort()
    return answer if answer else [-1]

print(solution(["X591X","X1X5X","X231X", "1XXX1"]))

#  추가 풀이
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solution(maps):
    col, row = len(maps), len(maps[0])
    visited = [[False]*row for _ in range(col)]
    
    answer = []
    
    for i in range(col) :
        for j in range(row) :
            if maps[i][j] != "X" and not visited[i][j] :
                period = 0
                q = [(j, i)]
                
                while q :
                    x, y = q.pop()
                    if visited[y][x] :
                        continue
                    visited[y][x] = True
                    period += int(maps[y][x])
                    
                    for k in range(4) :
                        ax, ay = x + dx[k], y + dy[k]
                        if -1 < ax < row and -1 < ay < col and maps[ay][ax] != "X" and not visited[ay][ax] :
                            q.append((ax, ay))
                    
                answer.append(period)
    
    return sorted(answer) if answer else [-1]