from typing import List
# from expense.split.split import Split


class Expense:
    def __init__(self, expense_id, description, amount, paid_by, splittype, split_details) -> None:
        self.expense_id = expense_id
        self.description = description
        self.amount = amount
        self.paid_by = paid_by
        self.splittype = splittype
        self.split_details = split_details
    


        