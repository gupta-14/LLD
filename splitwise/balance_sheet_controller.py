from expense.split.split import Split
from user.user import User
from balance import Balance

class BalanceSheetController:
    def update_user_expense_balance_sheet(self, expense_paid_by, splits, total_expense_amount):
        # update the total amount paid of the expense paid by user
        paid_by_user_expense_sheet = expense_paid_by.user_expense_balance_sheet
        paid_by_user_expense_sheet.total_payment += total_expense_amount

        for split in splits:
            user_owe = split.user
            owe_user_expense_sheet = user_owe.user_expense_balance_sheet
            owe_amount = split.amount_owe

            if expense_paid_by.user_id == user_owe.user_id:
                paid_by_user_expense_sheet.total_your_expense += owe_amount
            else:
                # update the balance of paid user
                paid_by_user_expense_sheet.total_you_get_back += owe_amount

                if user_owe.user_id in paid_by_user_expense_sheet.user_vs_balance:
                    user_owe_balance = paid_by_user_expense_sheet.user_vs_balance[user_owe.user_id]
                else:
                    user_owe_balance = Balance()
                    paid_by_user_expense_sheet.user_vs_balance[user_owe.user_id] = user_owe_balance

                user_owe_balance.amount_get_back += owe_amount

                # update the balance sheet of owe user
                owe_user_expense_sheet.total_you_owe += owe_amount
                owe_user_expense_sheet.total_your_expense += owe_amount

                if expense_paid_by.user_id in owe_user_expense_sheet.user_vs_balance:
                    user_paid_balance = owe_user_expense_sheet.user_vs_balance[expense_paid_by.user_id]
                else:
                    user_paid_balance = Balance()
                    owe_user_expense_sheet.user_vs_balance[expense_paid_by.user_id] = user_paid_balance

                user_paid_balance.amount_owe += owe_amount

    def show_balance_sheet_of_user(self, user):
        print("---------------------------------------")
        print("Balance sheet of user : " + user.user_id)

        user_expense_balance_sheet = user.user_expense_balance_sheet

        print("TotalYourExpense: " + str(user_expense_balance_sheet.total_your_expense))
        print("TotalGetBack: " + str(user_expense_balance_sheet.total_you_get_back))
        print("TotalYourOwe: " + str(user_expense_balance_sheet.total_you_owe))
        print("TotalPaymentMade: " + str(user_expense_balance_sheet.total_payment))

        for user_id, balance in user_expense_balance_sheet.user_vs_balance.items():
            print("userID:" + user_id + " YouGetBack:" + str(balance.amount_get_back) + " YouOwe:" + str(balance.amount_owe))

        print("---------------------------------------")