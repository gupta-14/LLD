from abc import ABCMeta, abstractmethod

class BasePizza(metaclass= ABCMeta):
    
    @abstractmethod
    def cost(self):
        pass