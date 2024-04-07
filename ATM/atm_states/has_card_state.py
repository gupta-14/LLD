from atm_states.atm_state import ATMState
# from atm import ATM
from card import Card
from transaction_type import TransactionType

class HasCardState(ATMState):
    def __init__(self) -> None:
        print("Insert your Card Pin Number")
    
    def insert_card(self, atm, card: Card):
        print("OOPS!! Something went wrong")

    def authenticate_pin(self, atm, card: Card, pin):
        from atm_states.select_operation_state import SelectOperationState
        is_correct_pin_entered = card.is_correct_pin_entered(pin)
        if is_correct_pin_entered:
            atm.set_current_atm_state(SelectOperationState())
        else:
            print("Invalid pin number")
            self.exit(atm)
        
    def exit(self, atm):
        from atm_states.idle_state import IdleState
        self.return_card()
        atm.set_current_atm_state(IdleState())
        print("EXIT DONE")
    
    def return_card(self):
        print("Please collect your card")

    def select_operation(self, atm, card: Card, transaction_type: TransactionType):
        print("OOPS!! Something went wrong")

    def cash_withdrawal(self, atm, card: Card, withdraw_amount):
        print("OOPS!! Something went wrong")

    def display_balance(self, atm, card: Card):
        print("OOPS!! Something went wrong")
