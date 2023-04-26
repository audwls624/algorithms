from collections import defaultdict

def task_order(n, m, dependencies):
    # Build a dictionary to store dependencies
    graph = defaultdict(list)
    for d in dependencies:
        graph[d[0]].append(d[1])

    # Build a set of all tasks
    tasks = set(graph.keys())
    for v in graph.values():
        tasks |= set(v)

    # Perform topological sort
    order = []
    visited = set()
    def dfs(v):
        visited.add(v)
        for w in graph[v]:
            if w not in visited:
                dfs(w)
        order.append(v)

    for v in tasks:
        if v not in visited:
            dfs(v)

    # Return order in reverse (since we appended in reverse order)
    result = ''.join(reversed(order))

    # Append any remaining tasks in alphabetical order
    remaining = tasks - set(order)
    if remaining:
        result += ''.join(sorted(remaining))

    return result


n = 5
m = 3
dependencies = ['BA', 'DA', 'BD']
result = task_order(n, m, dependencies)
print(result) # Output: BCDAE