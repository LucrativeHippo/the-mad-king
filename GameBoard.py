from time import time
from random import randrange
from Position import Pos

class MyTestObject:
    def __init__(self):
        self.p1 = True
        self.isKing = False
        assert self.p1 or not self.isKing

# TODO redesign this class for using less space
class dictBoard:
    def __init__(self):
        self.board = {}

    def start_state(self):
        self.board[Pos(6,0)] = 'D'
        self.board[Pos(6,6)] = 'D'
        self.board[Pos(6,3)] = 'K'
        for i in range(2,5):
            self.board[Pos(5,i)] = 'G'
        self.board[Pos(0,3)] = 'D'
        self.board[Pos(1,2)] = 'D'
        self.board[Pos(1,4)] = 'D'

    def __copy__(self):
        rv = dictBoard()
        rv.board = self.board.copy()
        return rv

    def copy(self):
        return self.__copy__()

    def __repr__(self):
        rStr = ""
        for x in range(0, 7):
            for y in range(0, 7):
                temp = self.board.get(Pos(6-x, y))
                if temp is None:
                    temp = '-'
                rStr += temp +" "
            rStr += "\n"
        rStr += "\n"
        return rStr


def legal_moves(board,piecePos):
    """
    Takes a piece position on the board, returns all legal moves
    :param board:
    :type board: dict()
    :param piecePos:
    :type piecePos: Pos
    :return: List of legal moves for a piece
    :rtype: [Pos]
    """
    rList = []
    #legal move for all pieces
    rList.append((piecePos+Pos(1,0)))
    rList.append((piecePos+Pos(-1,0)))
    rList.append((piecePos+Pos(0,1)))
    rList.append((piecePos+Pos(0,-1)))
    #if King
    if board.get(piecePos) == 'K':
        kList = []
        temp = 0
        for x in rList:
            if board.get(x) == 'G':
                if temp == 0:
                    kList.append((x+Pos(1,0)))
                elif temp == 1:
                    kList.append(x+Pos(-1,0))
                elif temp == 2:
                    kList.append(x+Pos(0,1))
                else:
                    kList.append(x+Pos(0,-1))
            temp += 1
        rList.extend(kList)
    elif board.get(piecePos) == 'D':
        rList.append((piecePos+Pos(1,1)))
        rList.append((piecePos+Pos(1,-1)))
        rList.append((piecePos+Pos(-1,1)))
        rList.append((piecePos+Pos(-1,-1)))
    return rList


def get_legal_moves(board,piecePos):
    move_list = legal_moves(board,piecePos)
    rList = list()
    while len(move_list)>0:
        x = move_list.pop()
        if(x.x>=0) & (x.y>=0) & (x.x<7) & (x.y<7) & (board.get(x) is None):
            rList.append(x)
    return rList


def move(board, piecePos, newPos):
    temp = board.pop(piecePos)
    board[newPos] = temp


# Modify this for use with the get_legal_moves function
def this_one(bClass, piecePos, newPos):
    l = get_legal_moves(bClass.board,piecePos)

    # **********************************************Use index
    b = dictBoard()
    b.board = bClass.board.copy()
    if l.count(newPos)>0:
        move(b.board,piecePos,newPos)
        return b
    else:
        print("NOOOOOOO! An illegal move!")


# TODO: add function to make board list, for all pieces whose turn it is





b = dictBoard()
b.start_state()
print(b)
print(get_legal_moves(b.board,Pos(6,0)))
print(this_one(b,Pos(6,3),Pos(6,4)))




#Tests
"""
class arrayBoard:
    def __init__(self):
        self.board = [[None for x in range(5)] for y in range(5)]

class testClass:
    def __init__(self):
        self.x = 0
        self.y = 0
    def __str__(self):
        return self.x+","+self.y
limit = 1000000
testvar = testClass()
def testDictBoard(b):
    print("Set:", end=' ')
    t_start = time()
    for x in range(limit):
        for y in range(5):
            for z in range(5):
                b[testvar] = MyTestObject()
    print(time()-t_start)
    print("Get:", end=' ')
    t_start = time()
    for x in range(limit):
        for y in range(5):
            for z in range(5):
                temp = b[testvar]
    print(time()-t_start)


def testDictBoardClass(b):
    print("Set:", end=' ')
    t_start = time()
    for x in range(limit):
        for y in range(5):
            for z in range(5):
                b.board[testvar] = MyTestObject()
    print(time()-t_start)
    print("Get:", end=' ')
    t_start = time()
    for x in range(limit):
        for y in range(5):
            for z in range(5):
                temp = b.board[testvar]
    print(time()-t_start)


def testArrayBoard(b):
    print("Set:", end=' ')
    t_start = time()
    for x in range(limit):
        for y in range(5):
            for z in range(5):
                b[y][z] = MyTestObject()
    print(time()-t_start)
    print("Get:", end=' ')
    t_start = time()
    for x in range(limit):
        for y in range(5):
            for z in range(5):
                temp = b[y][z]
    print(time()-t_start)


def testArrayBoardClass(b):
    print("Set:", end=' ')
    t_start = time()
    for x in range(limit):
        for y in range(5):
            for z in range(5):
                b.board[y][z] = MyTestObject()
    print(time()-t_start)
    print("Get:", end=' ')
    t_start = time()
    for x in range(limit):
        for y in range(5):
            for z in range(5):
                temp = b.board[y][z]
    print(time()-t_start)


varDict = {}
varArray = [[None for x in range(5)] for y in range(5)]

classBoard = dictBoard()
classArray = arrayBoard()
print("Variable defined dictionary:")
testDictBoard(varDict)
print("\nClass defined dictionary:")
testDictBoardClass(classBoard)

print("\nVariable defined array:")
testArrayBoard(varArray)
print("\nClass defined array:")
testArrayBoardClass(classArray)
"""