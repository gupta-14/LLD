from atm_states.atm_state import ATMState
from atm import ATM
from card import Card
from atm_states.idle_state import IdleState
from transaction_type import TransactionType

from amount_withdrawal.cash_withdrawal_processor import CashWithdrawProcessor
from amount_withdrawal.two_thousand_withdrawal_processor import TwoThousandWithdrawProcessor
from amount_withdrawal.five_hundred_withdrawal_processor import FiveHundredWithdrawProcessor
from amount_withdrawal.one_hundred_withdrawal_processor import OneHundredWithdrawProcessor

class CashWithdrawalState(ATMState):
    def __init__(self) -> None:
        print("Please Enter the withdrawal amount")

    def cash_withdrawal(self, atm: ATM, card: Card, withdraw_amount):
        if withdraw_amount > card.get_bank_balance():
            print(f"Insufficient fund in your bank account")
        elif withdraw_amount > atm.get_atm_balance():
            print(f"Insufficient Funds in the ATM Machine")
        else:
            card.deduct_bank_balance(withdraw_amount)
            atm.deduct_atm_balance(withdraw_amount)

        #using chain of responsibility for this logic, how many 2k Rs notes, how many 500 Rs notes etc, has to be withdrawal
        withdraw_processor = TwoThousandWithdrawProcessor(FiveHundredWithdrawProcessor(OneHundredWithdrawProcessor(None)))
        withdraw_processor.withdraw(atm, withdraw_amount)

        self.exit(atm)

    def exit(self, atm: ATM):
        self.return_card()
        atm.set_current_atm_state(IdleState())
        print("EXIT DONE")
    
    def return_card(self):
        print("Please collect your card")

    def insert_card(self, atm, card: Card):
        print("OOPS!! Something went wrong")

    def authenticate_pin(self, atm, card: Card, pin):
        print("OOPS!! Something went wrong")

    def select_operation(self, atm, card: Card, transaction_type: TransactionType):
        print("OOPS!! Something went wrong")

    def cash_withdrawal(self, atm, card: Card, withdraw_amount):
        print("OOPS!! Something went wrong")

    def display_balance(self, atm, card: Card):
        print("OOPS!! Something went wrong")
