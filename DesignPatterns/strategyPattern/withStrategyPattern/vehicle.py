from strategy.driveStrategy import DriveStrategy

class Vehicle(object):

    def __init__(self, driveObj: DriveStrategy):
        self.driveObj = driveObj

    def drive(self):
        self.driveObj.drive()