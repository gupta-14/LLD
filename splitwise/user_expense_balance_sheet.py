class UserExpenseBalanceSheet:
    def __init__(self) -> None:
        self.user_vs_balance = {}
        self.total_your_expense = 0
        self.total_payment = 0
        self.total_you_owe = 0
        self.total_you_get_back = 0

    def user_vs_balance(self) -> dict:
        return self._user_vs_balance

    def user_vs_balance(self, value: dict) -> None:
        self._user_vs_balance = value

    def total_your_expense(self) -> float:
        return self._total_your_expense

    def total_your_expense(self, value: float) -> None:
        self._total_your_expense = value

    def total_payment(self) -> float:
        return self._total_payment

    def total_payment(self, value: float) -> None:
        self._total_payment = value

    def total_you_owe(self) -> float:
        return self._total_you_owe

    def total_you_owe(self, value: float) -> None:
        self._total_you_owe = value

    def total_you_get_back(self) -> float:
        return self._total_you_get_back

    def total_you_get_back(self, value: float) -> None:
        self._total_you_get_back = value