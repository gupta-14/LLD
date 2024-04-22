from expense.split.expense_split import ExpenseSplit
from expense.split.split import Split

class PercentageExpenseSplit(ExpenseSplit):
    def validate_request(split_list: list[Split], total_amount):
        amount_present = 0
        for split in split_list:
            amount_present += split.get_amount_owe()
        if amount_present != total_amount:
            return False
        else:
            return True