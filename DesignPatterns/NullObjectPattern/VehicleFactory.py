from Car import Car
from NullVehicle import NullVehicle

class VehicleFactory:
    
    @staticmethod
    def getVehicleObject(typeOfVehicle: str):
        if (typeOfVehicle == "Car"):
            return Car()
        
        return NullVehicle()