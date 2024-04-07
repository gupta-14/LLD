class BankAccount:
    def __init__(self) -> None:
        self.balance = 0

    def withdrawal_balance(self, amount):
        self.balance -= amount
        