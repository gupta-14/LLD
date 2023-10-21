from Model.PlayingPiece import PlayingPiece
from Model.PieceType import PieceType

class PlayingPieceO(PlayingPiece):
    def __init__(self):
        super().__init__(PieceType.O)
