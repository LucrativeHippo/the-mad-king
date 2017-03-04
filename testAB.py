import GameBoard
import math




DEPTH_LIMIT = 5

class T:
    def __init__(self, childs=[], value=0):
        self.value = value
        self.children = childs


    def isTerminal(self):
        return len(self.children)==0

    def utility(self):
        return self.value

    def successors(self):
        return self.children

def board_value(state):
    return state.value



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
        move_list.append(minValue(s, alpha, beta))

    move = max(move_list)
    return move


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
    for (boardState) in state.successors():
        value = minValue(boardState, depth+1, alpha, beta)
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
    for (boardState) in state.successors():
        value = maxValue(boardState, depth + 1, alpha, beta)
        if value <= alpha:
            return beta
        beta = min(beta, value)
    return beta

l = [T([T(value=7),T(value=6),T(value=8)]),T([T(value=1),T(value=100),T(value=8)]),T([T(value=10),T(value=6),T(value=5)])]
t = T(l)

duck = T([T(value=4),T(value=1),T(value=8)])
print(minMaxFunction(duck))


