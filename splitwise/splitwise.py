from user.user_controller import UserController
from group.group_controller import GroupController
from balance_sheet_controller import BalanceSheetController
from user.user import User
from group.group import Group
from expense.split.split import Split
from expense.expense_split_type import ExpenseSplitType

class Splitwise:
    def __init__(self) -> None:
        self.user_controller = UserController()
        self.group_controller = GroupController()
        self.balance_sheet_controller = BalanceSheetController()
        
    def demo(self):
        self.setup_user_and_group()

        # adding members to group
        group = self.group_controller.get_group("G101")
        group.add_member(self.user_controller.get_user("U101"))
        group.add_member(self.user_controller.get_user("U102"))

        # create expense inside group
        splits = [
            Split(self.user_controller.get_user("U101"), 300),
            Split(self.user_controller.get_user("U102"), 300),
            Split(self.user_controller.get_user("U103"), 300)
        ]

        group.create_expense("Exp101", "Breakfast", 900, self.user_controller.get_user("U101"), ExpenseSplitType.EQUAL, splits)

        splits2  = [
            Split(self.user_controller.get_user("U101"), 400),
            Split(self.user_controller.get_user("U102"), 300)
        ]

        group.create_expense("Exp102", "Lunch", 700,self.user_controller.get_user("U102"), ExpenseSplitType.UNEQUAL, splits2)
        for user in self.user_controller.get_all_users():
            self.balance_sheet_controller.show_balance_sheet_of_user(user)


    def setup_user_and_group(self):
        self.add_users_to_splitwise()
        user1 = self.user_controller.get_user("U101")
        self.group_controller.create_group("G101", "Outing with friends", user1)

    def add_users_to_splitwise(self):
        #adding users
        user1 = User("U101", "user1")
        user2 = User("U102", "user2")
        user3 = User("U103", "user3")
        self.user_controller.add_user(user1)
        self.user_controller.add_user(user2)
        self.user_controller.add_user(user3)


if __name__ == "__main__":
    splitwise = Splitwise()
    splitwise.demo()