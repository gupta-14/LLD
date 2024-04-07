from bank_account import BankAccount

class Card:
    def __init__(self) -> None:
        self.card_number = None
        self.pin = 1234
        self.bank_account: BankAccount  = None

    def is_correct_pin_entered(self, pin):
        return pin == self.pin
    
    def get_bank_balance(self):
        return self.bank_account.balance

    def deduct_bank_balance(self, amount):
        self.bank_account.withdrawal_balance(amount)

    def set_bank_account(self, bank_account: BankAccount):
        self.bank_account = bank_account