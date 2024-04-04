from EmployeeDaoProxy import EmployeeDaoProxy
from EmployeeDo import EmployeeDo

def main():
    try:
        empObj = EmployeeDaoProxy()
        empObj.create("USER", EmployeeDo())
        print("operation success")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()