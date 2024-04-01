from Product.Vehicle import Vehicle
from User import User
from Location import Location
from ReservationType import ReservationType
from ReservationStatus import ReservationStatus

class Reservation:
    def __init__(self) -> None:
        self.reservationId = None
        self.user: User = None
        self.vehicle: Vehicle = None
        self.bookingDate = None
        self.dateBookedFrom = None
        self.dateBookedTo = None
        self.fromTimestamp = None
        self.toTimestamp = None
        self.pickUpLocation: Location = None
        self.dropLocation: Location = None
        self.reservationType: ReservationType = None
        self.reservationStatus: ReservationStatus = None
        self.location: Location = None

    def createReserve(self, user: User, vehicle: Vehicle):
        self.reservationId = 123121
        self.user = user
        self.vehicle = vehicle
        self.reservationType = ReservationType.DAILY