from abc import ABCMeta, abstractmethod

class WeightMachine(metaclass=ABCMeta):

    @abstractmethod
    def get_weight_in_pound(self):
        pass
