from expense.expense import Expense
from balance_sheet_controller import BalanceSheetController
from expense.split_factory import SplitFactory

class ExpenseController:
    def __init__(self) -> None:
        self.balance_sheet_controller: BalanceSheetController  = BalanceSheetController()

    def create_expense(self, expense_id, description, expense_amount, paid_by, splittype, split_details):
        expense_split = SplitFactory.get_split_object(splittype)
        if expense_split.validate_request(split_details, expense_amount):
            expense = Expense(expense_id, description, expense_amount, paid_by, splittype, split_details)
            self.balance_sheet_controller.update_user_expense_balance_sheet(paid_by, split_details, expense_amount)
            return expense
        
        else:
            raise Exception("Something went wrong")