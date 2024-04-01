from Product.VehicleType import VehicleType
from Product.Car import Car
from User import User
from Store import Store
from VehicleRentalSystem import VehicleRentalSystem
from Location import Location
from Reservation import Reservation
from Bill import Bill
from Payment import Payment

def main():
    users = addUsers()
    vehicles = addVehicles()
    stores = addStores(vehicles)
    rentalSystem = VehicleRentalSystem(users, stores)

    #user comes
    user = users[0]

    #user search store based on location
    location = Location("hsr", "Bangalore", "Karnataka", 403012)
    store: Store = rentalSystem.getStore(location)

    # get all vehicles you are intrested in based on different filters
    storeVehicles = store.getVehicles(VehicleType.CAR)

    #reservation the particular vehicle
    reservation: Reservation = store.createReservation(storeVehicles.get(0), user)

    #generate bill
    bill = Bill(reservation)

    #make payment
    payment = Payment()
    payment.payBill(bill)

    #trip completed, submit the vehicle and close the reservation
    store.completeReservation(reservation.reservationId)



def addUsers():
    users = []
    user1 = User()
    user1.setUserId(1)
    users.append(user1)
    return users

def addVehicles():
    vehicles = []
    vehicle1 = Car()
    vehicle1.setVehicleId(1)
    vehicle1.setVehicleType(VehicleType.CAR)

    vehicle2 = Car()
    vehicle2.setVehicleId(2)
    vehicle2.setVehicleType(VehicleType.CAR)

    vehicles.extend([vehicle1, vehicle2])
    return vehicles

def addStores(vehicles):
    stores = []
    store1 = Store()
    store1.storeId = 1
    store1.setVehicles(vehicles)
    stores.append(store1)
    return stores

if __name__ == "__main__":
    main()