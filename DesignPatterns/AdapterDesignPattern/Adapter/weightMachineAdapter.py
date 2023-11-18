from abc import ABCMeta, abstractmethod

class WeightMachineAdapter(metaclass=ABCMeta):

    @abstractmethod
    def get_weight_in_kg(self):
        pass
