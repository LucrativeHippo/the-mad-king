from time import time
from random import randrange
import unittest
from Position import Pos
import sys

class IllegalMoveError(Exception):
    pass

KING_SQUIRTLE_SQUAD = True
PUFFS_MAGICAL_DRAGON_SQUAD = False
WIDTH = 7
HEIGHT = 7
WIN_VALUE = 1000
WIN_FOR = KING_SQUIRTLE_SQUAD

class MyTestObject:
    def __init__(self):
        self.p1 = True
        self.isKing = False
        assert self.p1 or not self.isKing


# TODO redesign this class for using less space
class dictBoard:
    def __init__(self, state, player=PUFFS_MAGICAL_DRAGON_SQUAD):
        """

        :param state:
        :type state: dict
        :param player:
        """

        self.board = {}
        if state == None:
            self.board[Pos(6,0)] = 'D'
            self.board[Pos(6,6)] = 'D'
            self.board[Pos(6,3)] = 'K'
            for i in range(2,5):
                self.board[Pos(5,i)] = 'G'
            self.board[Pos(0,3)] = 'D'
            self.board[Pos(1,1)] = 'D'
            self.board[Pos(1,5)] = 'D'
        else:
            self.board = state

        self.whoseTurn = player
        self.cachedWin = False
        self.cachsedWinner = None

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

    def move(self, piecePos, newPos):
        temp = self.board.pop(piecePos)
        self.board[newPos] = temp

    def get(self,key):
        return self.board.get(key)

    def set(self,key,value):
        self.board[key] = value

    def isTerminal (self):
        return self.winFor(KING_SQUIRTLE_SQUAD) or self.winFor(PUFFS_MAGICAL_DRAGON_SQUAD) or (len(self.successors()) == 0)

    def legal_moves(self, piecePos):
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
        # legal move for all pieces
        rList.append((piecePos + Pos(1, 0)))
        rList.append((piecePos + Pos(-1, 0)))
        rList.append((piecePos + Pos(0, 1)))
        rList.append((piecePos + Pos(0, -1)))
        # if King
        # TODO better way to do this
        if self.board.get(piecePos) == 'K':
            kList = []
            temp = 0
            for x in rList:
                if self.board.get(x) == 'G':
                    if temp == 0:
                        kList.append((x + Pos(1, 0)))
                    elif temp == 1:
                        kList.append(x + Pos(-1, 0))
                    elif temp == 2:
                        kList.append(x + Pos(0, 1))
                    else:
                        kList.append(x + Pos(0, -1))
                temp += 1
            rList.extend(kList)
        elif self.board.get(piecePos) == 'D':
            rList.append((piecePos + Pos(1, 1)))
            rList.append((piecePos + Pos(1, -1)))
            rList.append((piecePos + Pos(-1, 1)))
            rList.append((piecePos + Pos(-1, -1)))
        return rList

    def get_legal_moves(self, piecePos):
        move_list = legal_moves(self.board, piecePos)
        rList = list()
        while len(move_list) > 0:
            x = move_list.pop()
            if (x.x >= 0) & (x.y >= 0) & (x.x < HEIGHT) & (x.y < WIDTH) & (self.board.get(x) is None):
                rList.append(x)
        return rList

    # TODO shrink get_legal_moves to legal_moves and call this in legal_moves


    # Modify this for use with the get_legal_moves function

    # TODO check if a guard is captured

    def this_one(self, piecePos, newPos):

        # TODO check whose turn and piece
        # TODO if king or gurads can capture a drangon

        if self.board.get(piecePos) == None:
            raise IllegalMoveError("Invalid Piece")

        l = get_legal_moves(self.board, piecePos)

        # **********************************************Use index
        b = dictBoard()
        b.board = self.board.copy()
        if (l.count(newPos) <= 0):
            raise IllegalMoveError("NOOOOOOO! An illegal move!")

        # TODO Count is terrible use index
        move(b.board,piecePos,newPos)
        return (b, piecePos, newPos)

    def successors(self):
        rList = []
        for p in self.teamPieces():
            for m in self.get_legal_moves(p):
                rList.append(self.this_one(p,m))
        return rList

    def winFor(self, player):
        if(self.cachedWin == False):
            won = False
            King_pos = None
            for key, value in pieces:
                if value == 'K':
                    King_pos = key
            assert King_pos != None

            if(player==KING_SQUIRTLE_SQUAD):
                pieces = self.board.items()
                if King_pos[0] == 0:
                    won = True
            elif(player==PUFFS_MAGICAL_DRAGON_SQUAD):
                raise Exception()
                # TODO check if king is captured
                # TODO cehck if tie
                    # case 1: two or less drangon king wins
                    # case 2: three or more drangons and no gaurds, dragons win
            if(won):
                self.cachedWin = True
                self.cachsedWinner = player
                return True
            else:
                return False
        else:
            return player == self.cachsedWinner


    def utility(self):
        if(self.winFor(WIN_FOR)):
            return WIN_VALUE
        elif(self.winFor(not WIN_FOR)):
            return -WIN_VALUE
        else:
            return 0








#TODO: add function to make board list, for all pieces whose turn it is

    def teamPieces(self):
        potentialMoves = []
        temp = self.board.items()
        if self.whoseTurn == KING_SQUIRTLE_SQUAD:
            for i in temp:
                if i[1] == 'G' or i[1] == 'K':
                    potentialMoves.append(i)
        else:
            for i in temp:
                if i[1] == 'D':
                    potentialMoves.append(i)

        return potentialMoves


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
teamMoves(b)




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