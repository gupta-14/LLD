from atm_states.atm_state import ATMState
# from atm import ATM
from card import Card
from atm_states.has_card_state import HasCardState
from transaction_type import TransactionType

class IdleState(ATMState):
    def insert_card(self, atm, card: Card):
        print("Card is inserted")
        atm.set_current_atm_state(HasCardState())

    def authenticate_pin(self, atm, card: Card, pin):
        print("OOPS!! Something went wrong")

    def select_operation(self, atm, card: Card, transaction_type: TransactionType):
        print("OOPS!! Something went wrong")

    def cash_withdrawal(self, atm, card: Card, withdraw_amount):
        print("OOPS!! Something went wrong")

    def display_balance(self, atm, card: Card):
        print("OOPS!! Something went wrong")

    def return_card(self):
        print("OOPS!! Something went wrong")

    def exit(self, atm):
        print("OOPS!! Something went wrong")    