from VehicleType import VehicleType
from Status import Status

class Vehicle:
    def __init__(self) -> None:
        self.vehicleId : int = None
        self.vehicleNumber : int = None
        self.vehicleType : VehicleType = None
        self.companyName : str = None
        self.modelName : str = None
        self.kmDriven : int = None
        self.manufacturingDate = None
        self.average = None
        self.cc = None
        self.dailyRentalCost = None
        self.hourlyRentalCost = None
        self.noOfSeat = None
        self.status : Status = None

    def getVehicleId(self):
        return self.vehicleId

    def setVehicleId(self, vehicleId):
        self.vehicleId = vehicleId
    
    def getVehicleNumber(self):
        return self.vehicleNumber

    def setVehicleNumber(self, vehicleNumber):
        self.vehicleNumber = vehicleNumber
    
    def getVehicleType(self):
        return self.vehicleType

    def setVehicleType(self, vehicleType):
        self.vehicleType = vehicleType
    
    def getCompanyName(self):
        return self.companyName

    def setCompanyName(self, companyName):
        self.companyName = companyName
    
    def getModelName(self):
        return self.modelName

    def setModelName(self, modelName):
        self.modelName = modelName
    
    def getKmDriven(self):
        return self.kmDriven

    def setKmDriven(self, kmDriven):
        self.kmDriven = kmDriven
    
    def getManufacturingDate(self):
        return self.manufacturingDate

    def setManufacturingDate(self, manufacturingDate):
        self.manufacturingDate = manufacturingDate
    
    def getAverage(self):
        return self.average

    def setAverage(self, average):
        self.average = average
    
    def getCc(self):
        return self.cc

    def setCc(self, cc):
        self.cc = cc
    
    def getDailyRentalCost(self):
        return self.dailyRentalCost

    def setDailyRentalCost(self, dailyRentalCost):
        self.dailyRentalCost = dailyRentalCost
        
    def getHourlyRentalCost(self):
        return self.hourlyRentalCost

    def setHourlyRentalCost(self, hourlyRentalCost):
        self.hourlyRentalCost = hourlyRentalCost
        
    def getNoOfSeat(self):
        return self.noOfSeat

    def setNoOfSeat(self, noOfSeat):
        self.noOfSeat = noOfSeat
        
    def getStatus(self):
        return self.status

    def setStatus(self, status):
        self.status = status
