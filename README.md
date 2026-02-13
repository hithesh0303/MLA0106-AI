# MLA0106-AI
# BFS-PseudoCode
FUNCTION BFS(graph, start_node)
    CREATE queue
    ENQUEUE start_node into queue
    CREATE visited set
    ADD start_node to visited
    CREATE traversal_order list
    WHILE queue is not empty DO
        current_node ← DEQUEUE from queue
        ADD current_node to traversal_order
        IF current_node exists in graph THEN
            FOR each neighbor in graph[current_node] DO
                IF neighbor not in visited THEN
                    ADD neighbor to visited
                    ENQUEUE neighbor into queue
                ENDIF
            ENDFOR
        ENDIF
    ENDWHILE
    RETURN traversal_order
END FUNCTION

# DFS-Pseudocode
FUNCTION DFS(graph, start_node)
    CREATE stack
    PUSH start_node into stack
    CREATE visited set
    ADD start_node to visited
    CREATE traversal_order list
    WHILE stack is not empty DO
        current_node ← POP from stack
        ADD current_node to traversal_order
        IF current_node exists in graph THEN
            FOR each neighbor in reverse order of graph[current_node] DO
                IF neighbor not in visited THEN
                    ADD neighbor to visited
                    PUSH neighbor into stack
                ENDIF
            ENDFOR
        ENDIF
    ENDWHILE
    RETURN traversal_order
END FUNCTION
