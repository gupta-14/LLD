from atm_states.atm_state import ATMState
# from atm import ATM
from card import Card
from atm_states.idle_state import IdleState
from atm_states.cash_withdrawal_state import CashWithdrawalState
from atm_states.check_balance_state import CheckBalanceState
from transaction_type import TransactionType

class SelectOperationState(ATMState):
    def __init__(self) -> None:
        self.show_operations()

    def select_operation(self, atm, card: Card, transaction_type: TransactionType):

        if transaction_type == TransactionType.WITHDRAWAL:
            atm.set_current_atm_state(CashWithdrawalState())
        
        elif transaction_type == TransactionType.BALANCE_INQUIRY:
            atm.set_current_atm_state(CheckBalanceState())
        
        else:
            print("Invalid Option")
            self.exit(atm)

    def exit(self, atm):
        self.return_card()
        atm.set_current_atm_state(IdleState())
        print("EXIT DONE")
    
    def return_card(self):
        print("Please collect your card")

    def show_operations(self):
        print("Please select the Operation")
        TransactionType.show_all_transaction_types()

    def insert_card(self, atm, card: Card):
        print("OOPS!! Something went wrong")

    def authenticate_pin(self, atm, card: Card, pin):
        print("OOPS!! Something went wrong")

    def cash_withdrawal(self, atm, card: Card, withdraw_amount):
        print("OOPS!! Something went wrong")

    def display_balance(self, atm, card: Card):
        print("OOPS!! Something went wrong")
