from Board import Board
from Dice import Dice
from Cell import Cell
from Player import Player
from collections import deque


class Game:
    def __init__(self):
        self.board: Board = None
        self.dice: Dice = None
        self.winner: Player = None
        self.playerList = deque()
        self.initializeGame()

    def initializeGame(self):
        self.board = Board(10, 5, 4)
        self.dice = Dice(1)
        self.winner = None
        self.addPlayers()

    def addPlayers(self):
        player1 = Player("p1", 0)
        player2 = Player("p2", 0)
        self.playerList.append(player1)
        self.playerList.append(player2)

    def startGame(self):
        while not self.winner:

            #check whose turn
            playerTurn = self.findPlayerTurn()
            print(f"Player turn is: {playerTurn.id} & current position is {playerTurn.currentPosition}")

            #roll the dice
            diceNumbers = self.dice.rollDice()

            #Get the new position
            playerNewPosition = playerTurn.currentPosition + diceNumbers
            playerNewPosition = self.jumpCheck(playerNewPosition)
            playerTurn.currentPosition = playerNewPosition

            #check for win condition
            if playerNewPosition >= len(self.board.cells)*len(self.board.cells)-1:
                self.winner = playerTurn
        print(f"WINNER IS: {self.winner.id}")

    def findPlayerTurn(self):
        playerTurns: Player = self.playerList.popleft()
        self.playerList.append(playerTurns)
        return playerTurns

    def jumpCheck(self, playerNewPosition):
        if playerNewPosition > len(self.board.cells)*len(self.board.cells)-1:
            return playerNewPosition

        cell: Cell = self.board.getCell(playerNewPosition)
        if cell.jump is not None and cell.jump.start == playerNewPosition:
            jumpBy = "ladder" if cell.jump.start < cell.jump.end else "snake"
            print(f"Jump done by: {jumpBy}")
            return cell.jump.end
        return playerNewPosition