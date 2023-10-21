from Model.PlayingPiece import PlayingPiece

class Board:
    def __init__(self, size):
        self.size = size
        self.board = [[None] * size for _ in range(size)]

    def addPiece(self, row, col, playingPiece: PlayingPiece):
        if self.board[row][col]:
            return False
        self.board[row][col] = playingPiece
        return True
    
    def getFreeCells(self):
        freeCells = []
        for i in range(self.size):
            for j in range(self.size):
                if not self.board[i][j]:
                    row_col = (i,j)
                    freeCells.append(row_col)
        return freeCells

    def printBoard(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] is not None:
                    print(self.board[i][j].pieceType.name, end="   ")
                else:
                    print("    ", end="")

                print(" | ", end="")

            print()