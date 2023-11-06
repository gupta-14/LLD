from Show import Show
from Payment import Payment
from Seat import Seat

class Booking:
    def __init__(self) -> None:
        self.show: Show = None
        self.bookedSeats: list[Seat] = None
        self.payment: Payment = None

    def getShow(self):
        return self.show
    
    def setShow(self, show):
        self.show = show

    def getBookedSeats(self):
        return self.bookedSeats
    
    def setBookedSeats(self, bookedSeats):
        self.bookedSeats = bookedSeats

    def getPayment(self):
        return self.payment
    
    def setPayment(self, payment):
        self.payment = payment                