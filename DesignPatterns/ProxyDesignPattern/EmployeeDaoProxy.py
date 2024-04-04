from EmployeeDo import EmployeeDo
from EmployeeDao import EmployeeDao
from EmployeeDaoImpl import EmployeeDaoImpl

class EmployeeDaoProxy(EmployeeDao):
    def __init__(self) -> None:
        self.employeeDaoObj = EmployeeDaoImpl()

    def create(self, client, obj: EmployeeDo):
        if client == "ADMIN":
            self.employeeDaoObj.create(client, obj)
            return
        raise Exception("Access Denied")

    def delete(self, client, employeeId):
        if client == "ADMIN":
            self.employeeDaoObj.delete(client, employeeId)
            return
        raise Exception("Access Denied")

    def get(self, client, employeeId):
        if client == "ADMIN" or client == "USER":
            return self.employeeDaoObj.get(client, employeeId)
        raise Exception("Access Denied")