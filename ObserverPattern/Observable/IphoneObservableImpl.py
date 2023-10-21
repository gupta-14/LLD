from Observable.StocksObservable import StockObservable
from Observer.NotificationAlertObserver import NotificationAlertObserver

class IphoneStockObservable(StockObservable):
    observerList : list[NotificationAlertObserver] = []

    def __init__(self):
        self.stockCount = 0

    def add(self, obj: NotificationAlertObserver):
        self.observerList.append(obj)
    
    def remove(self, obj: NotificationAlertObserver):
        self.observerList.remove(obj)
    
    def notify(self):
        for observer in self.observerList:
            observer.update()
    
    def setStockCount(self, newStockAdded):
        if not self.stockCount:
            self.notify()
        self.stockCount += newStockAdded
        
    
    def getStockCount(self):
        return self.stockCount