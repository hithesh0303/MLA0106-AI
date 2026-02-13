from collections import deque
CAP = (3, 5, 8)
START = (0, 0, 8)
GOAL = (None, 4, 4)  
def pour(state, i, j):
    s = list(state)
    amt = min(s[i], CAP[j] - s[j])
    s[i] -= amt
    s[j] += amt
    return tuple(s)
def next_states(state):
    res = []
    for i in range(3):
        for j in range(3):
            if i != j and state[i] > 0 and state[j] < CAP[j]:
                res.append(pour(state, i, j))
    return res
def is_goal(s):
    return s[1] == 4 and s[2] == 4
def solve():
    q = deque([(START, [START])])
    visited = {START}
    while q:
        state, path = q.popleft()
        if is_goal(state):
            return path
        for nxt in next_states(state):
            if nxt not in visited:
                visited.add(nxt)
                q.append((nxt, path + [nxt]))
    return None
ans = solve()
if ans:
    print("Steps:")
    for s in ans:
        print(s)
else:
    print("No solution")