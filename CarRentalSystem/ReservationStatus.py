from enum import Enum
class ReservationStatus(Enum):
    SCHEDULED = 'SCHEDULED'
    INPROGRES = 'INPROGRES'
    COMPLETED = 'COMPLETED'
    CANCELLED = 'CANCELLED'
