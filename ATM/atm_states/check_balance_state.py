from atm_states.atm_state import ATMState
from atm import ATM
from card import Card
from atm_states.idle_state import IdleState
from transaction_type import TransactionType

class CheckBalanceState(ATMState):
    def __init__(self) -> None:
        self.check_balance()

    def display_balance(self, atm: ATM, card: Card):
        print(f"Your Balance is {card.get_bank_balance()}")
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

 