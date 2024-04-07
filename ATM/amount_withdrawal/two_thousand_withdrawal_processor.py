from atm import ATM
from amount_withdrawal.cash_withdrawal_processor import CashWithdrawProcessor

class TwoThousandWithdrawProcessor(CashWithdrawProcessor):
    def __init__(self) -> None:
        super().__init__()

    def withdraw(self, atm: ATM, remaining_amount):
        required = remaining_amount//2000
        balance = remaining_amount%2000

        if required <= atm.get_no_of_two_thousand_notes():
            atm.deduct_no_of_two_thousand_notes(required)
        
        elif required> atm.get_no_of_two_thousand_notes():
            atm.deduct_no_of_two_thousand_notes(atm.get_no_of_two_thousand_notes())
            balance += (required-atm.get_no_of_two_thousand_notes())*2000
        
        if balance != 0:
            super().withdraw(atm, balance)