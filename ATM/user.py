from card import Card
from bank_account import BankAccount

class User:
    def __init__(self) -> None:
        self.card = None
        self.bank_account = None

    def get_card(self):
        return self.card

    def set_card(self, card: Card):
        self.card = card
    
    def get_bank_account(self):
        return self.bank_account

    def set_bank_account(self, bank_account: BankAccount):
        self.bank_account = bank_account
    
    

