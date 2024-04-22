from expense.expense_controller import ExpenseController
from expense.expense import Expense
from user.user import User

class Group:
    def __init__(self) -> None:
        self.group_id = None
        self.group_name = None
        self.group_members = []
        self.expense_list = []
        self.expense_controller = ExpenseController()

    def get_group_id(self):
        return self.group_id
    
    def get_group_name(self):
        return self.group_name
    
    def set_group_name(self, group_name):
        self.group_name = group_name

    def set_group_id(self, group_id):
        self.group_id = group_id
    
    def add_member(self, member: User):
        self.group_members.append(member)

    def create_expense(self, expense_id, description, amount, paid_by, splittype, split_details):
        expense = self.expense_controller.create_expense(expense_id, description, amount, paid_by, splittype, split_details)
        self.expense_list.append(expense)
        return expense