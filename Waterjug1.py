from collections import deque
CAP_A = 5  
CAP_B = 3   
TARGET = 4
def get_next_states(a, b):
    states = []
    states.append((CAP_A, b))   
    states.append((a, CAP_B))   
    states.append((0, b))    
    states.append((a, 0))       
    pour = min(a, CAP_B - b)
    states.append((a - pour, b + pour))
    pour = min(b, CAP_A - a)
    states.append((a + pour, b - pour))
    return states
def solve_water_jug():
    start = (0, 0)
    q = deque([(start, [start])])
    visited = set([start])
    while q:
        (a, b), path = q.popleft()
        if a == TARGET or b == TARGET:
            return path
        for nxt in get_next_states(a, b):
            if nxt not in visited:
                visited.add(nxt)
                q.append((nxt, path + [nxt]))
    return None
solution = solve_water_jug()
if solution:
    print("Steps:")
    for step in solution:
        print(step)
else:
    print("No solution found")