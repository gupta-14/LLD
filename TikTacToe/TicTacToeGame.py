from collections import deque
from Model.Player import Player
from Model.Board import Board
from Model.PieceType import PieceType
from Model.PlayingPieceX import PlayingPieceX
from Model.PlayingPieceO import PlayingPieceO

class TicTacToeGame:
    def __init__(self):
        self.initializeGame()

    def initializeGame(self):
        #creating 2 players
        self.players : Player = deque()
        crossPiece = PlayingPieceX()
        player1 = Player("Player1", crossPiece)

        zeroPiece = PlayingPieceO()
        player2 = Player("Player2", zeroPiece)
        
        self.players.append(player1)
        self.players.append(player2)
        
        #initialize Board
        self.gameBoard = Board(3)

    def startGame(self):
        noWinner = True
        while (noWinner):
            playerTurn = self.players.popleft()

            #get the free space from the board
            self.gameBoard.printBoard()
            freeSpaces = self.gameBoard.getFreeCells()
            if not freeSpaces:
                noWinner = False
                continue
            
            #read the user input
            print(f"Player: {playerTurn.name} Enter row, column: ")
            inputScanner = input()
            values = inputScanner.split(',')
            row = int(values[0])
            col = int(values[1])

            #place the piece
            pieceAddedSuccessfully = self.gameBoard.addPiece(row, col, playerTurn.playingPiece)
            if not pieceAddedSuccessfully:
                #player can not insert the piece into this cell, player has to choose another cell
                print("Incorrect position chosen, try again")
                self.players.appendleft(playerTurn)
                continue
            self.players.append(playerTurn)

            winner = self.isThereWinner(row, col, playerTurn.playingPiece.pieceType)
            if not winner:
                return playerTurn.name

        return "tie"    

    def isThereWinner(self, row, col, pieceType: PieceType):
        rowMatch = True
        columnMatch = True
        diagonalMatch = True
        antiDiagonalMatch = True

        #need to check in row
        for i in range(len(self.gameBoard.board)):
            if(self.gameBoard.board[row][i] == None or self.gameBoard.board[row][i].pieceType != pieceType):
                rowMatch = False

        #need to check in column
        for i in range(len(self.gameBoard.board)):
            if(self.gameBoard.board[i][col] == None or self.gameBoard.board[i][col].pieceType != pieceType):
                columnMatch = False


        #need to check diagonals
        for i ,j in zip(range(len(self.gameBoard.board)), range(len(self.gameBoard.board))):
            if (self.gameBoard.board[i][j] == None or self.gameBoard.board[i][j].pieceType != pieceType):
                diagonalMatch = False

        #need to check anti-diagonals
        for i,j in zip(range(len(self.gameBoard.board)), range(len(self.gameBoard.board)-1,0)):
            if (self.gameBoard.board[i][j] == None or self.gameBoard.board[i][j].pieceType != pieceType):
                antiDiagonalMatch = False

        return rowMatch or columnMatch or diagonalMatch or antiDiagonalMatch
