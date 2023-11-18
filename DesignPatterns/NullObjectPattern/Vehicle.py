from abc import ABCMeta, abstractmethod

class Vehicle(metaclass=ABCMeta):
    
    @abstractmethod
    def getTankCapacity(self):
        pass

    @abstractmethod
    def getSeatingCapacity(self):
        pass