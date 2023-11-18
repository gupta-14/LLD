from abc import ABCMeta, abstractmethod

class StockObservable(metaclass=ABCMeta):

    @abstractmethod
    def add(self, obj):
        pass

    @abstractmethod
    def remove(self, obj):
        pass

    @abstractmethod
    def notify(self):
        pass

    @abstractmethod
    def setStockCount(self, newStockAdded):
        pass

    @abstractmethod
    def getStockCount(self):
        pass