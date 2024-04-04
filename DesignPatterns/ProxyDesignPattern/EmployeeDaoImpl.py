from EmployeeDo import EmployeeDo
from EmployeeDao import EmployeeDao

class EmployeeDaoImpl(EmployeeDao):
    def __init__(self) -> None:
        super().__init__()

    def create(self, client: str, obj: EmployeeDo):
        print("Created a new row in the employee table")

    def delete(client: str, employeeId: int):
        print(f"Created a new row in the employee table: {employeeId}")

    def get(client: str, employeeId: int):
        print("Fetched data from the employee table")
        return EmployeeDo()