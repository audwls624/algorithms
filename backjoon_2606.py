n = int(input())
v = int(input())
graph = [[] for i in range(n+1)]
visited=[False]*(n+1)
for i in range(v):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited[1] = 1
stack = [1]

while stack:
    visiting = stack.pop()
    for nx in graph[visiting]:
        if not visited[nx]:
            stack.append(nx)
            visited[nx] = True
print(sum(visited)-1)

