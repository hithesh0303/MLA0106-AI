from collections import deque
CAP = (12, 8, 5)
TARGET = 6
def pour(state, i, j):
    s = list(state)
    amount = min(s[i], CAP[j] - s[j])
    s[i] -= amount
    s[j] += amount
    return tuple(s)
def next_states(state):
    res = []
    for i in range(3):
        for j in range(3):
            if i != j and state[i] > 0 and state[j] < CAP[j]:
                res.append(pour(state, i, j))
    return res
def solve():
    start = (12, 0, 0)
    q = deque([(start, [start])])
    visited = {start}
    while q:
        state, path = q.popleft()
        if TARGET in state:
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