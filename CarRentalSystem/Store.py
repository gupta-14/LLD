from VehicleInventoryManagement import VehicleInventoryManagement
from Location import Location
from Reservation import Reservation
from Product.Vehicle import Vehicle
from User import User

class Store:
    def __init__(self) -> None:
        self.storeId = None
        self.inventoryManagement : VehicleInventoryManagement = None
        self.storeLocation : Location = None
        self.reservations : Reservation = []

    def getVehicles(self):
        return self.inventoryManagement.getVehicles()
    
    #    addVehicles, update vehicles, use inventory management to update those.

    def setVehicles(self, vehicles):
        self.inventoryManagement = VehicleInventoryManagement(vehicles)
    
    def createReservation(self, vehicle : Vehicle, user : User):
        reservation = Reservation()
        reservation.createReserve(user, vehicle)
        self.reservations.append(reservation)
        return self.reservations
    
    def completeReservation(self, reservationId):
        # take out the reservation from the list and call complete the reservation method.
        return True
    
    #   update reservation
    
