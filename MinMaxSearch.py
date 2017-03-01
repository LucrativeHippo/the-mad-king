import GameBoard


def minMaxFunction(state):

    move, state = argmax(state.successors(state),
                         lambda x: minValue(x[0]))
    return move


def maxValue(state):
    if state.isTerminal():
        return
        value = -infinity
        for (boardState, location, move) in state.successors(state):
            value = min(value, minValue(boardState))
    return value

def minValue(state):
    if state.isTerminal():
        return
        value = inifinity
        for (boardState, location, move) in state.possibleMoves(state):
            value = max(value, maxValue(boardState))
    return value

def argmax(statePairList):
    maxUtil, maxMove = statePairList[0]
    for v,m in statePairList:
        if v > maxUtil:
            maxUtil, maxMove = v,m
    return maxUtil, maxMove

