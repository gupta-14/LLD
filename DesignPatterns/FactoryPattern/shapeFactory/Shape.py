from abc import ABCMeta, abstractmethod

class Shape(metaclass=ABCMeta):
    
    @abstractmethod
    def draw(self):
        pass