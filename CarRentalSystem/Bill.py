from Reservation import Reservation

class Bill:
    def __init__(self) -> None:
        self.reservation: Reservation = None
        self.totalBillAmount = self.computeBillAmount()
        self.isBillPaid = False
    
    def computeBillAmount():
        return 100.0