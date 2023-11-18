from VendingStates.impl.IdleState import IdleState  # Assuming IdleState is in the same directory
from Inventory import Inventory  # Assuming Inventory is in the same directory
from Coin import Coin  # Assuming Coin is in the same directory

class VendingMachine:
    def __init__(self) -> None:
        self.vending_machine_state = IdleState()
        self.inventory = Inventory(10)
        self.coin_list = []

    def get_vending_machine_state(self):
        return self.vending_machine_state

    def set_vending_machine_state(self, vending_machine_state):
        self.vending_machine_state = vending_machine_state

    def get_inventory(self):
        return self.inventory

    def set_inventory(self, inventory):
        self.inventory = inventory

    def get_coin_list(self):
        return self.coin_list

    def set_coin_list(self, coin_list):
        self.coin_list = coin_list