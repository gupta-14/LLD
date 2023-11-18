# from strategy.driveStrategy import DriveStrategy

class Vehicle(object):

    # driveObj = DriveStrategy()

    def __init__(self, driveObj):
        self.driveObj = driveObj

    def drive(self):
        self.driveObj.drive()