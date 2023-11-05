from Cell import Cell
from Jump import Jump
import random

class Board:
    def __init__(self, boardSize, numberOfSnakes, numberOfLadders):
        self.cells = []
        self.initializeCells(boardSize)
        self.addSnakesLadders(self.cells, numberOfSnakes, numberOfLadders)

    def initializeCells(self, boardSize):
        # self.cells = [[]]
        self.cells = [[Cell() for _ in range(boardSize)] for _ in range(boardSize)]

    def addSnakesLadders(self, cells, numberOfSnakes, numberOfLadders):
        while numberOfSnakes:
            snakeHead = random.randint(1, len(self.cells)*len(self.cells)-1)
            snakeTail = random.randint(1, len(self.cells)*len(self.cells)-1)

            if snakeTail >= snakeHead:
                continue

            snakeObj = Jump()
            snakeObj.start = snakeHead
            snakeObj.end = snakeTail

            cell = self.getCell(snakeHead)
            cell.jump = snakeObj

            numberOfSnakes -= 1

        while numberOfLadders:
            ladderStart = random.randint(1, len(self.cells)*len(self.cells)-1)
            ladderEnd = random.randint(1, len(self.cells)*len(self.cells)-1)

            if ladderStart >= ladderEnd:
                continue

            ladderObj = Jump()
            ladderObj.start = ladderStart
            ladderObj.end = ladderEnd

            cell = self.getCell(ladderStart)
            cell.jump = ladderObj

            numberOfLadders -= 1
            
    def getCell(self, playerPosition):
        boardRow = playerPosition//len(self.cells)
        boardCol = playerPosition%len(self.cells)
        return self.cells[boardRow][boardCol]
        