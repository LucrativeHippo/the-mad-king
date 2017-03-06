import GameBoard
import math
from AlphaBeta import board_value
from Position import Pos


DEPTH_LIMIT = 3


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
    for s in state.successors():
        move_list.append((maxValue(s[0]), s[1]))
    move = max(move_list, key=lambda x: x[0])
    return move[1]

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
    for (boardState, (location, move)) in state.successors():
        temp = minValue(boardState, depth + 1)
        if temp >= value:
            value = temp
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
    for (boardState, (location, move)) in state.successors():
        temp = maxValue(boardState, depth + 1)
        if temp <= value:
            value = temp
    return value


b = dictBoard(None)
total_time = time()
for i in range(0,50):
    t_start = time()
    x, y = minMaxFunction(b)
    move1 = b.this_one(x, y)[0]
    print("move",i+1)
    print(move1)
    b = move1
    print(time() - t_start)
print("cumulative time:", total_time)



