from abc import ABC, abstractmethod
from EmployeeDo import EmployeeDo

class EmployeeDao(ABC):
    @abstractmethod
    def create(client, obj: EmployeeDo):
        pass

    @abstractmethod
    def delete(client, employeeId):
        pass

    @abstractmethod
    def get(client, employeeId):
        pass