from strategy.sportsDriveStrategy import SportsDriveStrategy
from vehicle import Vehicle

class SportsVehicle(Vehicle):
    def __init__(self):
        super().__init__(SportsDriveStrategy())
