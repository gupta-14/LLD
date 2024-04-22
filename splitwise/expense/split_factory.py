from expense.expense_split_type import ExpenseSplitType
from expense.split.equal_expense_split import EqualExpenseSplit
from expense.split.unequal_expense_split import UnequalExpenseSplit
from expense.split.percentage_expense_split import PercentageExpenseSplit

class SplitFactory:

    @staticmethod
    def get_split_object(split_type: ExpenseSplitType):
        if split_type == ExpenseSplitType.EQUAL:
            return EqualExpenseSplit()
        elif split_type == ExpenseSplitType.UNEQUAL:
            return UnequalExpenseSplit()
        elif split_type == ExpenseSplitType.PERCENTAGE:
            return PercentageExpenseSplit()
        else:
            return None