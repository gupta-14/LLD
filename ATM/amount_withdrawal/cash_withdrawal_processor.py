from atm import ATM

class CashWithdrawProcessor:
    def __init__(self) -> None:
        self.cash_withdrawal_processor = CashWithdrawProcessor()

    def withdraw(self, atm: ATM, remaining_amount):
        if self.cash_withdrawal_processor:
            self.cash_withdrawal_processor.withdraw(atm, remaining_amount)