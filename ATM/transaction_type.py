from enum import Enum

class TransactionType(Enum):
    WITHDRAWAL = "Withdrawal"
    DEPOSIT = "Deposit"
    BALANCE_INQUIRY = "Balance Inquiry"

    @staticmethod
    def show_all_transaction_types():
        for transaction_type in TransactionType:
            print(transaction_type.value)