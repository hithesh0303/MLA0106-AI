import heapq
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E'],
    'C': ['F','E'],
    'D': ['F'],
    'E': ['H'],
    'F': ['G'],
    'G': [],
    'H': ['G']
}

h = {
    'A': 40,
    'B': 32,
    'C': 25,
    'D': 35,
    'E': 19,
    'F': 17,
    'G': 0,
    'H': 10,

}
def greedy_best_first(start, goal):
    pq = [(h[start], start, [start])]
    visited = set()
    while pq:
        _, node, path = heapq.heappop(pq)
        if node == goal:
            return path
        if node in visited:
            continue
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                heapq.heappush(pq, (h[neighbor], neighbor, path + [neighbor]))
    return None
print("Path:", greedy_best_first('A', 'G'))