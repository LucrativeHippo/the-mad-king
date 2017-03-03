def boardValue(board):
    if board.isTerminal:
        raise Exception()
    dragonCount = 0
    gaurdCount = 0
    for i in board.values():
        if i == 'D':
            dragonCount += 1
        elif i == 'G':
            gaurdCount +=1



    # TODO the scoer varies as the king close to the end of the board and if a drangon is on the way instead of a clear path