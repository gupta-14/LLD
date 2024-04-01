class User:
    def __init__(self) -> None:
        self.userId = None
        self.userName = None
        self.drivingLicence = None

    # getter setter
    def getUserId(self):
        return self.userId

    def setUserId(self, userId):
        self.userId = userId
    
    def getUserName(self):
        return self.userName

    def setUserName(self, userName):
        self.userName = userName
    
    def getDrivingLicence(self):
        return self.drivingLicence

    def setDrivingLicence(self, drivingLicence):
        self.drivingLicence = drivingLicence
    