class Balance:
    def __init__(self):
        self.amount_owe = 0
        self.amount_get_back = 0

    def amount_owe(self) -> float:
        return self._amount_owe

    def amount_owe(self, value: float) -> None:
        self._amount_owe = value

    def amount_get_back(self) -> float:
        return self._amount_get_back

    def amount_get_back(self, value: float) -> None:
        self._amount_get_back = value
