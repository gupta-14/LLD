from Model.PlayingPiece import PlayingPiece
from Model.PieceType import PieceType

class PlayingPieceX(PlayingPiece):
    def __init__(self):
        super().__init__(PieceType.X)
