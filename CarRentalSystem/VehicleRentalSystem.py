from Location import Location
class VehicleRentalSystem:
    def __init__(self, users, stores) -> None:
        self.users = users
        self.stores = stores

    #crud operations

    def getStore(self, location: Location):
        # based on location, we will filter out the store from stores
        return self.stores[0]