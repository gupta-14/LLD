from abc import ABC, abstractmethod
from card import Card
# from atm import ATM
from transaction_type import TransactionType

class ATMState(ABC):
    
    @abstractmethod
    def insert_card(self, atm, card: Card):
        print("OOPS!! Something went wrong")

    @abstractmethod
    def authenticate_pin(self, atm, card: Card, pin):
        print("OOPS!! Something went wrong")

    @abstractmethod
    def select_operation(self, atm, card: Card, transaction_type: TransactionType):
        print("OOPS!! Something went wrong")

    @abstractmethod
    def cash_withdrawal(self, atm, card: Card, withdraw_amount):
        print("OOPS!! Something went wrong")

    @abstractmethod
    def display_balance(self, atm, card: Card):
        print("OOPS!! Something went wrong")

    @abstractmethod
    def return_card(self):
        print("OOPS!! Something went wrong")

    @abstractmethod
    def exit(self, atm):
        print("OOPS!! Something went wrong")
