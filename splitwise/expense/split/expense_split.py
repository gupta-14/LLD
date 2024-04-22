from abc import ABC, abstractmethod

class ExpenseSplit(ABC):
    
    @abstractmethod
    def validate_request():
        pass