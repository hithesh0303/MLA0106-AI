import heapq
graph = {
    'S': [('A', 3), ('D', 4)],
    'A': [('D', 5), ('B', 4)],
    'B': [('C', 4), ('E', 5)],
    'D': [('E', 2)],
    'E': [('F', 4)],
    'F': [('G', 3.5)],
    'C': [],
    'G': []
}
h = {
    'S': 11.5,
    'A': 10.1,
    'B': 5.8,
    'C': 3.4,
    'D': 9.2,
    'E': 7.1,
    'F': 3.5,
    'G': 0
}
def astar(start, goal):
    pq = [(h[start], 0, start, [start])]
    while pq:
        f, g, node, path = heapq.heappop(pq)
        if node == goal:
            return path, g
        for neighbor, cost in graph[node]:
            g_new = g + cost
            f_new = g_new + h[neighbor]
            heapq.heappush(pq, (f_new, g_new, neighbor, path + [neighbor]))
    return None, -1
path, cost = astar('S', 'G')
print("Path:", path)
print("Cost:", cost)