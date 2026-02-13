scores = [2,3,5,9,0,1,7,5]
def alphabeta(depth, index, isMax, alpha, beta):
    if depth == 3:
        return scores[index]
    if isMax:
        value = -999
        for i in range(2):
            value = max(value,
                        alphabeta(depth+1, index*2+i, False, alpha, beta))
            alpha = max(alpha, value)
            if beta <= alpha:
                break
        return value
    else:
        value = 999
        for i in range(2):
            value = min(value,
                        alphabeta(depth+1, index*2+i, True, alpha, beta))
            beta = min(beta, value)
            if beta <= alpha:
                break
        return value
print("Optimal value:", alphabeta(0, 0, True, -999, 999))