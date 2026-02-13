graph = {
    '1': ['2', '3'],
    '2': ['4', '5'],
    '3': [],
    '4': [],
    '5': []
}
def bfs(graph, start_node):
    queue = [start_node]
    visited = {start_node}
    traversal_order = []
    while queue:
        current_node = queue.pop(0)
        traversal_order.append(current_node)
        if current_node in graph:
            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
    return traversal_order
start_node = '1'
bfs_result = bfs(graph, start_node)
print(f"BFS from node '{start_node}': {bfs_result}")