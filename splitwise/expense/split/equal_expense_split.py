from expense.split.expense_split import ExpenseSplit
from expense.split.split import Split

class EqualExpenseSplit(ExpenseSplit):
    def validate_request(self, split_list: list[Split], total_amount):
        amount_present = total_amount//len(split_list)
        for split in split_list:
            if amount_present != split.get_amount_owe():
                return False
        return True