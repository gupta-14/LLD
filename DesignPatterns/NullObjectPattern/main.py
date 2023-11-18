from VehicleFactory import VehicleFactory

def printVehicleDetails(vehicle):
    print(f"Seating Capacity : {vehicle.getSeatingCapacity()}")
    print(f"Tank Capacity : {vehicle.getTankCapacity()}")

vehicle = VehicleFactory.getVehicleObject("Car")
printVehicleDetails(vehicle)

