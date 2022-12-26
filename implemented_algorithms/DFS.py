import sys
sys.setrecursionlimit(10000)


def dfs(x,y):
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
    if (0 <= nx < N) and (0 <= ny < M):
        if matrix[nx][ny]==1:
            matrix[nx][ny]==-1
            dfs(nx,ny)

T=int(input())
for _ in range(T):
    M,N,K=map(int,input().split())
    matrix=[[0]*M for _ in range(N)]
    count=0

    for _ in range(K):
        m,n = map(int,input().split())
        matrix[n][m]=1
    
    for i in range(N):
        for j in range(M):
            if matrix[i][j]>0:
                dfs(i,j)
                count+=1
print(count)



