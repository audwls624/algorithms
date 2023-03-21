import sys
N_t = int(input())
sys.setrecursionlimit(10000)

def DFS(x, y):
    if x < 0 or y < 0 or x >= M or y >= N:
        return False

    dx = [-1 , 1, 0, 0]
    dy = [0, 0, 1, -1]

    if matrix[x][y] == 1:
        matrix[x][y] = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            DFS(nx, ny)


for i in range(N_t):
    M, N, K = map(int, input().split())
    matrix = [[0] * N for _ in range(M)]
    count = 0

    for j in range(K):
        x, y = map(int, input().split())
        matrix[x][y] = 1

    for _x in range(M):
        for _y in range(N):
            if matrix[_x][_y] == 1:
                DFS(_x, _y)
                count += 1
                
    print(count)
