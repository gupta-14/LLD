from atm import ATM
from user import User
from card import Card
from bank_account import BankAccount
from transaction_type import TransactionType

class ATMRoom:
    def __init__(self) -> None:
        self.atm = None
        self.user: User = None
    
    def main(self):
        self.initialize()
        self.atm.print_current_atm_status()
        self.atm.get_current_atm_state().insert_card(self.atm, self.user.card)
        self.atm.get_current_atm_state().authenticate_pin(self.atm, self.user.card, 1234)
        self.atm.get_current_atm_state().select_operation(self.atm, self.user.card, TransactionType.WITHDRAWAL)
        self.atm.get_current_atm_state().cash_withdrawal(self.atm, self.user.card, 2700)
        self.atm.print_current_atm_status()

    def initialize(self):
        self.atm = ATM().get_atm_object()
        self.atm.set_atm_balance(3500, 1, 2, 5)
        self.user = self.create_user()

    def create_user(self):
        user = User()
        user.set_card(self.create_card())
        return user

    def create_card(self):
        card = Card()
        card.set_bank_account(self.create_bank_account())
        return card
    
    def create_bank_account(self):
        bank_account = BankAccount()
        bank_account.balance = 3000
        return bank_account


if __name__ == "__main__":
    atmroom = ATMRoom()
    atmroom.main()
