from time import time
from random import randrange
import unittest
from Position import Pos


class IllegalMoveError(Exception):
    pass


class NotDoneError(Exception):
    pass

# The true king of the water
KING_SQUIRTLE_SQUAD = True
# The false king and traitor
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


class dictBoard:
    def __init__(self, state, player=PUFFS_MAGICAL_DRAGON_SQUAD):
        """
        Board dictionary with minimax functions
        :param state:
        :type state: dict{}
        :param player:
        :type player: bool
        :rtype: None
        """

        self.board = {}

        self.whoseTurn = player
        self.cachedWin = False
        self.cachedWinner = None
        if state is None:
            # This code runs only once, more efficient way to write it but shouldn't matter
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
            for p in self.board.items():
                if self.is_squirtle_surround(p[0]) & (p[1] is 'G'):
                    self.board.pop(p)

            if self.whoseTurn is KING_SQUIRTLE_SQUAD:
                for p in self.teamPieces(PUFFS_MAGICAL_DRAGON_SQUAD):
                    if self.is_dragon_surrounded(p):
                        self.board[p] = 'd'
            else:
                # part of PUFFS_MAGICAL_DRAGON_SQUAD
                for p in self.board.keys():
                    self.board[p] = self.board[p].upper()

    def __copy__(self):
        rv = dictBoard({})
        rv.board = self.board.copy()
        return rv

    def copy(self):
        return self.__copy__()

    def __repr__(self):
        r_str = ""
        for x in range(0, HEIGHT):
            for y in range(0, WIDTH):
                temp = self.board.get(Pos(HEIGHT-1-x, y))
                if temp is None:
                    temp = '-'
                r_str += temp + " "
            r_str += "\n"
        r_str += "\n"
        return r_str

    def __move(self, piecePos, newPos):
        """
        Dumb __move function. Moves any contents of piecePos to any newPos. Doesn't follow rules
        :param piecePos: Position of piece
        :type piecePos: Pos
        :param newPos: Position to __move to
        :type newPos: Pos
        :rtype: None
        """
        temp = self.board.pop(piecePos)
        self.board[newPos] = temp

    def get(self, key):
        return self.board.get(key)

    def set(self, key, value):
        """
        Sets value in board dictionary
        :param key: Board position
        :type key: Position.Pos
        :param value: 'K' or 'D' or 'G' or None
        :type value: char
        """
        self.board[key] = value

    @property
    def king_pos(self):
        """

        :return: Position of king
        :rtype: Pos
        """
        pieces = self.board.items()
        for key, value in pieces:
            if value == 'K':
                return key

    def winFor(self, player):
        """
        Returns end value of board,
        :param player:
        :type player: bool
        :return: Win value, +1000 if player, -1000 if not player, 0 if tie
        :rtype: int
        """
        if self.cachedWin is False:
            won = False
            king_pos = self.king_pos
            assert king_pos is not None

            if player is KING_SQUIRTLE_SQUAD:
                if king_pos.x == 0:
                    won = True
            elif player is PUFFS_MAGICAL_DRAGON_SQUAD:
                if (len(self.get_legal_moves(king_pos)) is 0) \
                        & (self.is_squirtle_surround(king_pos)):
                    won = True
                # TODO check if tie
                    # case 1: two or less drangon king wins
                    # case 2: three or more drangons and no gaurds, dragons win
            if won:
                self.cachedWin = True
                self.cachedWinner = player
                return True
            else:
                return False
        else:
            return player is self.cachedWinner

    def isTerminal(self):
        return self.winFor(KING_SQUIRTLE_SQUAD) \
               or self.winFor(PUFFS_MAGICAL_DRAGON_SQUAD) \
               or (len(self.successors()) == 0)

    def is_squirtle_surround(self, piecePos):
        """

        :param self:
        :type self:
        :param piecePos:
        :type piecePos:
        :return:
        :rtype:
        """
        gk_count = 0
        for i in (-1, 1):
            if self.get(piecePos + Pos(i, 0)) in ('d', 'D'):
                gk_count += 1
            if self.get(piecePos + Pos(0, i)) in ('d', 'd'):
                gk_count += 1
            if gk_count > 2:
                return True
        return False

    def is_dragon_surrounded(self, piecePos):
        gk_count = 0
        for i in (-1, 1):
            if self.get(piecePos + Pos(i, 0)) in ('K', 'G'):
                gk_count += 1
            if self.get(piecePos + Pos(0, i)) in ('K', 'G'):
                gk_count += 1
            if gk_count > 1:
                return True
        return False

    def legal_moves(self, piecePos):
        """
        Takes a piece position on the board, returns all legal moves
        :param board:
        :type board: {"Pos":Char}
        :param piecePos:
        :type piecePos: Pos
        :return: List of legal moves for a piece
        :rtype: list[Pos]
        """
        rList = []
        # legal __move for all pieces
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

    """
    def get_neighbours_pos(self, piecePos):
        return [piecePos + Pos(1, 0),
                piecePos + Pos(0, 1),
                piecePos - Pos(1, 0),
                piecePos - Pos(0, 1)]
    """

    def get_legal_moves(self, piecePos):
        """
        Creates list of legal moves from a piece
        :param piecePos: position of a piece
        :type piecePos: Position.Pos
        :return: List of legal moves for this piece
        :rtype: list[Pos]
        """
        move_list = self.legal_moves(piecePos)
        rList = list()
        while len(move_list) > 0:
            x = move_list.pop()
            if (x.x >= 0) & (x.y >= 0) & (x.x < HEIGHT) & (x.y < WIDTH) & (self.board.get(x) in (None, 'd')):
                rList.append(x)
        return rList


    # Modify this for use with the get_legal_moves function

    def this_one(self, piecePos, newPos):
        """

        :param piecePos: Piece to be moved
        :type piecePos: Pos
        :param newPos: Position to __move to
        :type newPos: Pos
        :return:
        :rtype: (dictBoard, Pos, Pos)
        """
        if self.board.get(piecePos) is None:
            raise IllegalMoveError("Invalid Piece")

        l = self.get_legal_moves(piecePos)

        # **********************************************Use index
        r_board = dictBoard(self.board.copy())
        if l.count(newPos) <= 0:
            raise IllegalMoveError("NOOOOOOO! An illegal __move!")

        # fixme count is terrible use index
        r_board.__move(piecePos, newPos)
        r_board.whoseTurn = not r_board.whoseTurn
        return r_board, piecePos, newPos

    def teamPieces(self, team=None):
        """
        Gives list of all pieces of current player
        :type team: bool
        :return: list of all pieces of current player
        :rtype: list[Pos]
        """
        if team is None:
            team = self.whoseTurn
        potential_moves = []
        temp = self.board.items()
        if team == KING_SQUIRTLE_SQUAD:
            for i in temp:
                if i[1] == 'G' or i[1] == 'K':
                    potential_moves.append(i)
        else:
            for i in temp:
                if i[1] == 'D':
                    potential_moves.append(i)

        return potential_moves

    def successors(self):
        """
        Returns list of all moves for all pieces of the current player
        :return: list of all moves for the current players turn
        :rtype: [dictBoard, Pos, Pos]
        """
        rList = []
        for p in self.teamPieces():
            for m in self.get_legal_moves(p):
                rList.append(self.this_one(p, m))
        return rList

    def utility(self):
        if self.winFor(WIN_FOR):
            return WIN_VALUE
        else:
            return -WIN_VALUE











class BoardTests(unittest.TestCase):

    def test_board_init(self):
        tbAlpha = dictBoard({}).board
        self.assertEqual(tbAlpha, {}, "Board is not a dictionary.")
        self.assertEqual(len(tbAlpha), 0, "Board is not empty on init.")
        self.assertIsNone(tbAlpha.get(Pos(6,0)))

    def test_start_board(self):
        foo = dictBoard(None)
        board = foo.board
        self.assertEqual(board.get(Pos(6,0)), 'D')
        self.assertIsNone(board.get(Pos(5,0)))
        self.assertEqual(board.get(Pos(6,3)),'K')

    def test_move_board(self):
        foo = dictBoard(None)
        board = foo.board
        with self.assertRaises(IllegalMoveError):
            foo.this_one(Pos(6,3),Pos(6,6)) # legal piece, illegal __move
        with self.assertRaises(IllegalMoveError):
            foo.this_one(Pos(6,5),Pos(5,5)) # illegal piece, legal __move
        self.assertNotEqual(foo.get(Pos(6,4)),'K')
        foo2 = foo.this_one(Pos(6,3),Pos(6,4))[0]
        self.assertEqual(foo2.get(Pos(6,4)),'K')
        self.assertNotEqual(foo2.get(Pos(6,3)),'K')


if __name__ == '__main__':
    unittest.main

"""
b = dictBoard(None)
print(b)
print(b.get_legal_moves(Pos(6,3)))
print(b.this_one(Pos(6,3),Pos(6,4))[0])
b.teamPieces()
b.utility()
"""



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