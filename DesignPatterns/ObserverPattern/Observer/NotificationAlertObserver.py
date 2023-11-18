from abc import ABCMeta, abstractmethod

class NotificationAlertObserver(metaclass=ABCMeta):

    @abstractmethod
    def update(self):
        pass