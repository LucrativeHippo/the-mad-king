from time import time
from random import randrange
import unittest
from Position import Pos
import sys

HEIGHT = 7
WIDTH = 7


class IllegalMoveError(Exception):
    pass

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
        for x in range(0, HEIGHT):
            for y in range(0, WIDTH):
                temp = self.board.get(Pos(HEIGHT-1-x, y))
                if temp is None:
                    temp = '-'
                rStr += temp +" "
            rStr += "\n"
        rStr += "\n"
        return rStr

    def get(self,key):
        return self.board.get(key)

    def set(self,key,value):
        self.board[key] = value


def legal_moves(board,piecePos):
    """
    Takes a piece position on the board, returns all legal moves
    :param board:
    :type board: {"Pos":Char}
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
    # if King
    # TODO better way to do this
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

# TODO shrink get_legal_moves to legal_moves and call this in legal_moves


def get_legal_moves(board,piecePos):
    move_list = legal_moves(board,piecePos)
    rList = list()
    while len(move_list)>0:
        x = move_list.pop()
        if(x.x>=0) & (x.y>=0) & (x.x<HEIGHT) & (x.y<WIDTH) & (board.get(x) is None):
            rList.append(x)
    return rList


def move(board, piecePos, newPos):
    temp = board.pop(piecePos)
    board[newPos] = temp


# Modify this for use with the get_legal_moves function
def this_one(bClass, piecePos, newPos):
    if bClass.board.get(piecePos) == None:
        raise IllegalMoveError("Invalid Piece")

    l = get_legal_moves(bClass.board,piecePos)

    # **********************************************Use index
    b = dictBoard()
    b.board = bClass.board.copy()
    if (l.count(newPos) <= 0):
        raise IllegalMoveError("NOOOOOOO! An illegal move!")

    # TODO Count is terrible use index
    move(b.board,piecePos,newPos)
    return b


# TODO: add function to make board list, for all pieces whose turn it is




class BoardTests(unittest.TestCase):
    foo = dictBoard()
    foo.start_state()
    board = foo.board

    def test_board_init(self):
        tbAlpha = dictBoard().board
        self.assertEqual(tbAlpha, {}, "Board is not a dictionary.")
        self.assertEqual(len(tbAlpha), 0, "Board is not empty on init.")
        self.assertIsNone(tbAlpha.get(Pos(6,0)))

    def test_start_board(self):
        self.assertEqual(self.board.get(Pos(6,0)), 'D')
        self.assertIsNone(self.board.get(Pos(5,0)))
        self.assertEqual(self.board.get(Pos(6,3)),'K')

    def test_move_board(self):
        with self.assertRaises(IllegalMoveError):
            this_one(self.foo,Pos(6,3),Pos(6,6)) # legal piece, illegal move
        with self.assertRaises(IllegalMoveError):
            this_one(self.foo,Pos(6,5),Pos(5,5)) # illegal piece, legal move
        print(self.foo)
        self.assertNotEqual(self.foo.get(Pos(6,4)),'K')
        self.foo = this_one(self.foo,Pos(6,3),Pos(6,4))
        print(self.foo)
        self.assertEqual(self.foo.get(Pos(6,4)),'K')
        self.assertNotEqual(self.foo.get(Pos(6,3)),'K')


if __name__ == '__main__':
    unittest.main

b = dictBoard()
b.start_state()
print(b)
print(get_legal_moves(b.board,Pos(6,3)))
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