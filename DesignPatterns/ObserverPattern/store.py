from Observable.IphoneObservableImpl import IphoneStockObservable
from Observer.MobileAlertObserverImpl import MobileAlertObserverImpl
from Observer.EmailAlertObserverImpl import EmailAlertObserverImpl

iphoneStockObservable = IphoneStockObservable()
observer1 = EmailAlertObserverImpl("shubham@gmail.com", iphoneStockObservable)
observer2 = EmailAlertObserverImpl("shubham.gpt@gmail.com", iphoneStockObservable)
observer3 = MobileAlertObserverImpl("shubham_gpt", iphoneStockObservable)

iphoneStockObservable.add(observer1)
iphoneStockObservable.add(observer2)
iphoneStockObservable.add(observer3)

iphoneStockObservable.setStockCount(10)
iphoneStockObservable.setStockCount(0)
iphoneStockObservable.setStockCount(100)