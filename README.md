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

# UCS Pseudocode
FUNCTION BFS(graph,start_node)
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
END FOR
ENDIF
END WHILE
RETURN traversal_order
END FUNCTION

# Greedy best first search Pseudocode
FUNCTION GREEDY_BEST_FIRST(start,goal)
CREATE priority_queue pq
INSERT (h[start],start,[start]) into pq
CREATE visited set
WHILE pq is not empty DO
(_,node,path) ← REMOVE_MIN(pq)
IF node = goal THEN
RETURN path
ENDIF
IF node in visited THEN
CONTINUE
ENDIF
ADD node to visited
FOR each neighbor in graph[node] DO
IF neighbor not in visited THEN
INSERT (h[neighbor],neighbor,path+[neighbor]) into pq
ENDIF
END FOR
END WHILE
RETURN NULL
END FUNCTION

# A* search Pseudocode
FUNCTION A_STAR(start,goal)
CREATE priority_queue pq
INSERT (h[start],0,start,[start]) into pq
WHILE pq not empty DO
(f,g,node,path) ← REMOVE_MIN(pq)
IF node = goal THEN
RETURN path,g
ENDIF
FOR each (neighbor,cost) in graph[node] DO
g_new ← g + cost
f_new ← g_new + h[neighbor]
INSERT (f_new,g_new,neighbor,path+[neighbor]) into pq
END FOR
END WHILE
RETURN NULL,-1
END FUNCTION

# Mini Max
FUNCTION MINIMAX(depth,index,isMax)
IF depth = MAX_DEPTH THEN
RETURN score[index]
ENDIF
IF isMax = TRUE THEN
RETURN MAX(
MINIMAX(depth+1,index*2,FALSE),
MINIMAX(depth+1,index*2+1,FALSE)
)
ELSE
RETURN MIN(
MINIMAX(depth+1,index*2,TRUE),
MINIMAX(depth+1,index*2+1,TRUE)
)
ENDIF
END FUNCTION

# Alpha–Beta pruning Pseudocode
FUNCTION ALPHABETA(depth,index,isMax,alpha,beta)
IF depth = MAX_DEPTH THEN
RETURN scores[index]
ENDIF
IF isMax THEN
value ← -∞
FOR i ← 0 to 1 DO
value ← MAX(value, ALPHABETA(depth+1,index*2+i,FALSE,alpha,beta))
alpha ← MAX(alpha,value)
IF beta ≤ alpha THEN
BREAK
ENDIF
END FOR
RETURN value
ELSE
value ← +∞
FOR i ← 0 to 1 DO
value ← MIN(value, ALPHABETA(depth+1,index*2+i,TRUE,alpha,beta))
beta ← MIN(beta,value)
IF beta ≤ alpha THEN
BREAK
ENDIF
END FOR
RETURN value
END IF
END FUNCTION

# Water Jug problem
CAP_A←5
CAP_B←3
TARGET←4
FUNCTION WATER_JUG_BFS()
start_state←(0,0)
create empty queue Q
create empty set VISITED
ENQUEUE(start_state,[start_state])into Q
add start_state to VISITED
WHILE Q not empty DO
(a,b),path←DEQUEUE Q
IF a=TARGET OR b=TARGET THEN
RETURN path
ENDIF
NEXT_STATES={
(CAP_A,b),
(a,CAP_B),
(0,b),
(a,0),
(a−min(a,CAP_B−b),b+min(a,CAP_B−b)),
(a+min(b,CAP_A−a),b−min(b,CAP_A−a))
}
FOR each S in NEXT_STATES DO
IF S not in VISITED THEN
add S to VISITED
ENQUEUE(S,path+S)into Q
ENDIF
ENDFOR
ENDWHILE
RETURN"No solution"
END FUNCTION
