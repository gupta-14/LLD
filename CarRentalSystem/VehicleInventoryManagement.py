from Product.Vehicle import Vehicle

class VehicleInventoryManagement:
    def __init__(self, vehicles) -> None:
        self.vehicles = vehicles

    def getVehicles(self):
        return self.vehicles
    
    def setVehicles(self, vehicles: Vehicle):
        self.vehicles = vehicles