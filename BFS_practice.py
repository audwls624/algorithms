from queue import Queue

class Graph:
    def __init__(self, vertex_num):
        # 인접 리스트로 구현
        self.adj_list = [[] for _ in range(vertex_num)]
        # 방문 여부 체크
        self.visited = [False for _ in range(vertex_num)]
    
    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def init_visited(self):
        for i in range(len(self.visited)):
            self.visited[i] = False

    def bfs(self, v):
        q = Queue()
        self.init_visited()

        q.put(v)
        self.visited[v] = True

        while not q.empty():
            v = q.get()
            print(v, end=" ")
            adj_v = self.adj_list[v]
            for u in adj_v:
                if not self.visited[u]:
                    q.put(u)
                    self.visited[u] = True

    def dfs_recursion(self, v):
        print(v, end=" ")
        self.visited[v] = True

        adj_v = self.adj_list[v]
        for u in adj_v:
            if not self.visited[u]:
                self.dfs_recursion(u)
    
    def dfs_inter(self, v):
        stack = []
        self.init_visited()

        stack.append(v)
        self.visited[v] = True
        print(v, end = " ")

        is_visited = False
        while stack:
            is_visited = False
            v = stack[-1]
            adj_v = self.adj_list[v]
            for u in adj_v:
                if not self.visited[u]:
                    stack.append(u)
                    self.visited[u] = True
                    print(u, end=" ")
                    is_visited = True
                    break
            if not is_visited:
                stack.pop()


    def dfs(self, v):
        self.init_visited()
        self.dfs_recursion(v)
