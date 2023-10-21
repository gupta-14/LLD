from Model.PlayingPiece import PlayingPiece

class Player:
    def __init__(self, name, playingPiece: PlayingPiece):
        self.name = name
        self.playingPiece = playingPiece

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name
    
    def setPlayingPiece(self, playingPiece):
        self.playingPiece = playingPiece

    def getPlayingPiece(self):
        return self.playingPiece
