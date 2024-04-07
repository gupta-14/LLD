from atm_states.atm_state import ATMState
from atm_states.idle_state import IdleState

class ATM:
    _atm_instance = None

    def __init__(self) -> None:
        self.current_atm_state: ATMState = None
        self.atm_balance: int = 0
        self.no_of_two_thousand_notes: int = 0
        self.no_of_five_hundred_notes: int = 0
        self.no_of_one_hundred_notes: int = 0

    @classmethod
    # defining singleton initialization
    def get_atm_object(cls):
        if  cls._atm_instance is None:
            cls._atm_instance = ATM()
            cls._atm_instance.current_atm_state = IdleState()
            
        return cls._atm_instance

    def set_current_atm_state(self, atm_state: ATMState):
        self.current_atm_state = atm_state

    def get_current_atm_state(self):
        return self.current_atm_state

    def get_atm_balance(self):
        return self.atm_balance

    def set_atm_balance(self, atm_balance, no_of_two_thousand_notes, no_of_five_hundred_notes, no_of_one_hundred_notes):
        self.atm_balance: int = atm_balance
        self.no_of_two_thousand_notes = no_of_two_thousand_notes
        self.no_of_five_hundred_notes = no_of_five_hundred_notes
        self.no_of_one_hundred_notes = no_of_one_hundred_notes

    def get_no_of_two_thousand_notes(self):
        return self.no_of_two_thousand_notes
    
    def get_no_of_five_hundred_notes(self):
        return self.no_of_five_hundred_notes
    
    def get_no_of_one_hundred_notes(self):
        return self.no_of_one_hundred_notes    

    def deduct_atm_balance(self, amount):
        self.atm_balance -= amount
    
    def deduct_no_of_two_thousand_notes(self, no_of_two_thousand_notes):
        self.no_of_two_thousand_notes -= no_of_two_thousand_notes

    def deduct_no_of_five_hundred_notes(self, no_of_five_hundred_notes):
        self.no_of_five_hundred_notes -= no_of_five_hundred_notes

    def deduct_no_of_one_hundred_notes(self, no_of_one_hundred_notes):
        self.no_of_one_hundred_notes -= no_of_one_hundred_notes

    def print_current_atm_status(self):
        print(f"Balance: {self.atm_balance}")
        print(f"2k Notes: {self.no_of_two_thousand_notes}")
        print(f"500 Notes: {self.no_of_five_hundred_notes}")
        print(f"100 Notes: {self.no_of_one_hundred_notes}")