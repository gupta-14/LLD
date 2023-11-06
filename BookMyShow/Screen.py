from Seat import Seat

class Screen:
    def __init__(self) -> None:
        self.screenId = None
        self.seats : list[Seat] = []

    def getScreenId(self):
        return self.screenId
    
    def setScreenId(self, screenId):
        self.screenId = screenId

    def getSeats(self):
        return self.seats
    
    def setSeats(self, seats):
        self.seats = seats        