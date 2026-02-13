import heapq
graph = {
    'S': [('A', 1), ('G', 12)],
    'A': [('C', 1), ('B', 1)],
    'C': [('G', 2), ('D', 1)],
    'B': [('D', 3)],
    'D': [('G', 3)],
    'G': []
}
def ucs(start, goal):
    pq = [(0, start)]
    visited = set()
    while pq:
        cost, node = heapq.heappop(pq)
        if node == goal:
            return cost
        if node in visited:
            continue
        visited.add(node)
        for neighbor, w in graph.get(node, []):
            heapq.heappush(pq, (cost + w, neighbor))
    return -1
print("Minimum cost:", ucs('S', 'G'))