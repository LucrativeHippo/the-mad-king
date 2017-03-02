import GameBoard
import math

DEPTH_LIMIT = 1


def minMaxFunction(state):
    """

    :param state:
    :type state: GameBoard.dictBoard
    :return:
    :rtype: (int, Position.Pos)
    """
    if state.isTerminal():
        return state.utility()
    move, state = argmax(state.successors(state),
                         lambda x: minValue(x[0]))
    return move


def maxValue(state, depth=0):
    """

    :param state:
    :type state: GameBoard.dictBoard
    :return:
    """
    if state.isTerminal() or depth == DEPTH_LIMIT:
        return state.utility()
    value = -math.inf
    for (boardState, location, move) in state.successors(state):
        value = max(value, minValue(boardState))
    return value

def minValue(state, depth=0):
    """

    :param state:
    :type state: GameBoard.dictBoard
    :return:
    """
    if state.isTerminal() or depth == DEPTH_LIMIT:
        return state.utility()

    value = math.inf
    for (boardState, location, move) in state.possibleMoves(state):
        value = min(value, maxValue(boardState))
    return value

def argmax(statePairList):
    maxUtil, maxMove = statePairList[0]
    for v,m in statePairList:
        if v > maxUtil:
            maxUtil, maxMove = v,m
    return maxUtil, maxMove

