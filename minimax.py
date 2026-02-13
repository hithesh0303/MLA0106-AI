scores = [2,3,5,9,0,1,7,5]
def minimax(depth, index, isMax):
    if depth == 3:
        return scores[index]
    if isMax:
        return max(
            minimax(depth+1, index*2, False),
            minimax(depth+1, index*2+1, False)
        )
    else:
        return min(
            minimax(depth+1, index*2, True),
            minimax(depth+1, index*2+1, True)
        )
print("Optimal value:", minimax(0, 0, True))