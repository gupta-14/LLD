from Observer.NotificationAlertObserver import NotificationAlertObserver
from Observable.StocksObservable import StockObservable

class MobileAlertObserverImpl(NotificationAlertObserver):
    def __init__(self, userName, observable: StockObservable):
        self.observable = observable
        self.userName = userName

    def update(self):
        self.sendMsgOnMobile("Product is in stock")
    
    def sendMsgOnMobile(self, msg):
        print(f"{msg} -> Msg sent to {self.userName}")
    