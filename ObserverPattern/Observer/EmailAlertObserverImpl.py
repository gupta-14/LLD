from Observer.NotificationAlertObserver import NotificationAlertObserver
from Observable.StocksObservable import StockObservable

class EmailAlertObserverImpl(NotificationAlertObserver):
    def __init__(self, emailId, observable: StockObservable):
        self.observable = observable
        self.emailId = emailId

    def update(self):
        self.sendEmail("Product is in stock")
    
    def sendEmail(self, msg):
        print(f"{msg} -> Mail sent to {self.emailId}")
