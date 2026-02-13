graph = {
    '1': ['2', '3'],
    '2': ['4','5'],
    '3': []
}
def dfs(graph, start_node):
    stack = [start_node]
    visited = {start_node}
    traversal_order = []
    while stack:
        current_node = stack.pop()
        traversal_order.append(current_node)
        if current_node in graph:
            for neighbor in reversed(graph[current_node]):
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
    return traversal_order
start_node = '1'
dfs_result = dfs(graph, start_node)
print(f"DFS from node '{start_node}': {dfs_result}")