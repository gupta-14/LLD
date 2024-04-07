from amount_withdrawal.cash_withdrawal_processor import CashWithdrawProcessor
from atm import ATM

class FiveHundredWithdrawProcessor(CashWithdrawProcessor):
    def __init__(self) -> None:
        super().__init__()

    def withdraw(self, atm: ATM, remaining_amount):
        required = remaining_amount//500
        balance = remaining_amount%500

        if required <= atm.get_no_of_five_hundred_notes():
            atm.deduct_no_of_five_hundred_notes(required)
        
        elif required> atm.get_no_of_five_hundred_notes():
            atm.deduct_no_of_five_hundred_notes(atm.get_no_of_five_hundred_notes())
            balance += (required-atm.get_no_of_five_hundred_notes())*500
        
        if balance != 0:
            super().withdraw(atm, balance)