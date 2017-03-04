from GameBoard import dictBoard


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
    for i in board.values():
        if i == 'D':
            dragonCount += 1
        elif i == 'G':
            guardCount += 1

    return dragonCount*(-100) + guardCount*100 + (6-board.king_pos.x)*100



    # TODO the scoer varies as the king close to the end of the board and if a drangon is on the way instead of a clear path