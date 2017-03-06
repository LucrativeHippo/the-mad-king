from time import time
from GameBoard import dictBoard
import math
from Position import Pos
DEPTH_LIMIT = 2
def board_value(board):
    """

    :param board:
    :type board: dictBoard
    :return:
    :rtype:
    """
    if board.isTerminal():
        return board.utility()
    dragonCount = 0
    guardCount = 0
    for i in board.board.values():
        if i == 'D':
            dragonCount += 1
        elif i == 'G':
            guardCount += 1

    if board.king_clear:
        kclear = 50
    else:
        kclear = -50


    return ((5-dragonCount)*(100)) + ((3-guardCount)*-100) \
           + (6-board.king_pos.x)*20 + board.get_neighbours_guards(board.king_pos)*20 \
           + kclear + board.num_little_ds()*100

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
    alpha = -math.inf
    beta = math.inf
    for s in state.successors():
        move_list.append((minValue(s[0], alpha, beta), s[1]))
    move = max(move_list, key=lambda x: x[0])
    return move[1]

def maxValue(state, alpha, beta, depth=0):
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
        value = minValue(boardState, alpha, beta, depth + 1)
        if value >= beta:
            return alpha
        alpha = max(alpha, value)
    return alpha

def minValue(state, alpha, beta, depth=0):
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
        value = maxValue(boardState, alpha, beta, depth+1)
        if value <= alpha:
            return beta
        beta = min(beta, value)

    return beta

b = dictBoard(None)
total_time = time()
for i in range(0,100):
    t_start = time()
    x, y = minMaxFunction(b)
    move1 = b.this_one(x, y)[0]
    print("move",i+1)
    print(move1)
    b = move1
    print(time() - t_start)
print("cumulative time:", time() - total_time)

# print(move4)





    # TODO the scoer varies as the king close to the end of the board and if a drangon is on the way instead of a clear path