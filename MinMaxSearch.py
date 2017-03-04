import GameBoard
import math
from AlphaBeta import board_value

DEPTH_LIMIT = 1


def minMaxFunction(state):
    """

    :param state: Current GameBoard
    :type state: GameBoard.dictBoard
    :return: utility of move, original position, move position
    :rtype: (int, (Position.Pos, Position.Pos))
    """
    if state.isTerminal():
        return state.utility(), None

    move_list = []
    for s in state.successors(state):
        move_list.append(maxValue(s[0], s[1]))
    move = max(move_list, key=lambda x: x[0])[1]
    print(move_list)
    print(move)
    return move


def maxValue(state, depth=0):
    """

    :param state:
    :type state: GameBoard.dictBoard
    :return:
    """
    if state.isTerminal():
        return state.utility()

    if depth == DEPTH_LIMIT:
        return board_value(state)

    value = -math.inf
    for (boardState, location, move) in state.successors(state):
        value = max(minValue(boardState, depth+1))
    return value


def minValue(state, depth=0):
    """

    :param state:
    :type state: GameBoard.dictBoard
    :return:
    """
    if state.isTerminal():
        return state.utility()

    if depth == DEPTH_LIMIT:
        return board_value(state)

    value = math.inf
    for (boardState, location, move) in state.successors(state):
        value = min(value, maxValue(boardState, depth+1))
    return value





