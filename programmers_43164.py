# tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
link = {ticket[0]:[] for ticket in tickets}

for ticket in tickets:
    link[ticket[0]].append(ticket[1])
    link[ticket[0]].sort(reverse=True)

stack = ["ICN"]
route = []
while stack:
    point = stack.pop()
    route.append(point)
    if link.get(point):
        _next = link[point].pop()
        stack.append(_next)


print(route)

