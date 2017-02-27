from time import time
from random import randrange


class MyTestObject:
    def __init__(self):
        self.p1 = True
        self.isKing = False
        assert self.p1 or not self.isKing


class StandardDictBoard:
    def __init__(self):
        self.numKings = 1
        self.numDragons = 5
        self.numGuards = 3
        self.board = {1: 'D', 2: '-', 3: '-', 4: 'K', 5: '-', 6: '-', 7: 'D',
                     8: '-', 9: '-', 10: 'G', 11: 'G', 12: 'G', 13: '-', 14: '-',
                     15: '-', 16: '-', 17: '-', 18: '-', 19: '-', 20: '-', 21: '-',
                     22: '-', 23: '-', 24: '-', 25: '-', 26: '-', 27: '-', 28: '-',
                     29: '-', 30: '-', 31: '-', 32: '-', 33: '-', 34: '-', 35: '-',
                     36: '-', 37: 'D', 38: '-', 39: 'D', 40: '-', 41: 'D', 42: '-',
                     43: '-', 44: '-', 45: '-', 46: '-', 47: '-', 48: '-', 49: '-'}

    def toBoard(self):
        for key in range(1,8):
            print(self.board.get(key), end='')
        print("")
        for key in range(8,15):
            print(self.board.get(key), end='')
        print("")
        for key in range(15,22):
            print(self.board.get(key), end='')
        print("")
        for key in range(22,29):
            print(self.board.get(key), end='')
        print("")
        for key in range(29,36):
            print(self.board.get(key), end='')
        print("")
        for key in range(36,43):
            print(self.board.get(key), end='')
        print("")
        for key in range(43,50):
            print(self.board.get(key), end='')

    def isValidLocation(self, location):
        return (location > 0 )and(location < 50)

    def spaceEmpty(self, location):
        return self.board.get(location) == '-'

    def validMoves(self, location):
        listMoves = list()
        if self.board.get(location) == 'K':
            if location % 7 == 0:
                if self.spaceEmpty(location-1)and self.isValidLocation(location-1):
                    listMoves.append(location-1)
                if self.spaceEmpty(location-7)and self.isValidLocation(location-7):
                    listMoves.append(location-7)
                if self.spaceEmpty(location+7) and self.isValidLocation(location+7):
                    listMoves.append(location+7)
                if self.board.get(location-1)\
                        == 'G'and self.spaceEmpty(location-2)and self.isValidLocation(location-2):
                    listMoves.append(location - 2)
                if self.board.get(location-7)\
                        == 'G'and self.spaceEmpty(location-14)and self.isValidLocation(location-14):
                    listMoves.append(location - 14)
                if self.board.get(location+7)\
                        == 'G'and self.spaceEmpty(location+14)and self.isValidLocation(location+14):
                    listMoves.append(location + 14)

            elif location % 7 == 1:
                if self.spaceEmpty(location+1)and self.isValidLocation(location+1):
                    listMoves.append(location+1)
                if self.spaceEmpty(location-7)and self.isValidLocation(location-7):
                    listMoves.append(location-7)
                if self.spaceEmpty(location+7) and self.isValidLocation(location+7):
                    listMoves.append(location+7)
                if self.board.get(location+1) \
                        == 'G'and self.spaceEmpty(location+2)and self.isValidLocation(location+2):
                    listMoves.append(location + 2)
                if self.board.get(location-7) \
                        == 'G'and self.spaceEmpty(location-14)and self.isValidLocation(location-14):
                    listMoves.append(location - 14)
                if self.board.get(location+7) \
                        == 'G'and self.spaceEmpty(location+14)and self.isValidLocation(location+14):
                    listMoves.append(location + 14)
            else:
                if self.spaceEmpty(location-1)and self.isValidLocation(location-1):
                    listMoves.append(location-1)
                if self.spaceEmpty(location-7)and self.isValidLocation(location-7):
                    listMoves.append(location-7)
                if self.spaceEmpty(location+7) and self.isValidLocation(location+7):
                    listMoves.append(location+7)
                if self.spaceEmpty(location+1)and self.isValidLocation(location+1):
                    listMoves.append(location+1)
                if self.board.get(location-1) \
                        == 'G'and self.spaceEmpty(location-2)and self.isValidLocation(location-2):
                    listMoves.append(location - 2)
                if self.board.get(location-7)\
                        == 'G'and self.spaceEmpty(location-14)and self.isValidLocation(location-14):
                    listMoves.append(location - 14)
                if self.board.get(location+7)\
                        == 'G'and self.spaceEmpty(location+14)and self.isValidLocation(location+14):
                    listMoves.append(location + 14)
                if self.board.get(location+1)\
                        == 'G'and self.spaceEmpty(location+2)and self.isValidLocation(location+2):
                    listMoves.append(location + 2)

        if self.board.get(location) == 'G':
            if location % 7 == 0:
                if self.spaceEmpty(location-1)and self.isValidLocation(location-1):
                    listMoves.append(location-1)
                if self.spaceEmpty(location-7)and self.isValidLocation(location-7):
                    listMoves.append(location-7)
                if self.spaceEmpty(location+7) and self.isValidLocation(location+7):
                    listMoves.append(location+7)

            elif location % 7 == 1:
                if self.spaceEmpty(location+1)and self.isValidLocation(location+1):
                    listMoves.append(location+1)
                if self.spaceEmpty(location-7)and self.isValidLocation(location-7):
                    listMoves.append(location-7)
                if self.spaceEmpty(location+7) and self.isValidLocation(location+7):
                    listMoves.append(location+7)
            else:
                if self.spaceEmpty(location-1)and self.isValidLocation(location-1):
                    listMoves.append(location-1)
                if self.spaceEmpty(location-7)and self.isValidLocation(location-7):
                    listMoves.append(location-7)
                if self.spaceEmpty(location+7) and self.isValidLocation(location+7):
                    listMoves.append(location+7)
                if self.spaceEmpty(location+1)and self.isValidLocation(location+1):
                    listMoves.append(location+1)

        if self.board.get(location) == 'D':
            if location % 7 == 0:
                if self.spaceEmpty(location-1)and self.isValidLocation(location-1):
                    listMoves.append(location-1)
                if self.spaceEmpty(location-7)and self.isValidLocation(location-7):
                    listMoves.append(location-7)
                if self.spaceEmpty(location+7) and self.isValidLocation(location+7):
                    listMoves.append(location+7)
                if self.spaceEmpty(location+6) and self.isValidLocation(location+6):
                    listMoves.append(location+6)
                if self.spaceEmpty(location-8) and self.isValidLocation(location-8):
                    listMoves.append(location-8)

            elif location % 7 == 1:
                if self.spaceEmpty(location+1)and self.isValidLocation(location+1):
                    listMoves.append(location+1)
                if self.spaceEmpty(location-7)and self.isValidLocation(location-7):
                    listMoves.append(location-7)
                if self.spaceEmpty(location+7) and self.isValidLocation(location+7):
                    listMoves.append(location+7)
                if self.spaceEmpty(location-6) and self.isValidLocation(location-6):
                    listMoves.append(location-6)
                if self.spaceEmpty(location+8) and self.isValidLocation(location+8):
                    listMoves.append(location+8)
            else:
                if self.spaceEmpty(location-1)and self.isValidLocation(location-1):
                    listMoves.append(location-1)
                if self.spaceEmpty(location-7)and self.isValidLocation(location-7):
                    listMoves.append(location-7)
                if self.spaceEmpty(location+7) and self.isValidLocation(location+7):
                    listMoves.append(location+7)
                if self.spaceEmpty(location+1)and self.isValidLocation(location+1):
                    listMoves.append(location+1)
                if self.spaceEmpty(location-6) and self.isValidLocation(location-6):
                    listMoves.append(location-6)
                if self.spaceEmpty(location+8) and self.isValidLocation(location+8):
                    listMoves.append(location+8)
                if self.spaceEmpty(location+6) and self.isValidLocation(location+6):
                    listMoves.append(location+6)
                if self.spaceEmpty(location-8) and self.isValidLocation(location-8):
                    listMoves.append(location-8)

        if self.board.get(location) == '-':
            print("there is no piece on this space")

        return listMoves

    def terminalState(self, kingpos):
        if self.numDragons <= 2 and self.numGuards > 0:
            return True  # might return 1000
        if self.numGuards == 0 and self.numDragons > 2:
            return True  # must check if king has clear path to end, might return -1000
        # check if king captured

class dictBoard:
    def __init__(self):
        self.board={}


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
"""
testDictBoard(varDict)
print("\nClass defined dictionary:")
testDictBoardClass(classBoard)

print("\nVariable defined array:")
testArrayBoard(varArray)
print("\nClass defined array:")
testArrayBoardClass(classArray)
"""
startBoard = StandardDictBoard()
startBoard.toBoard()
listMoves = startBoard.validMoves(1)
print(listMoves)
