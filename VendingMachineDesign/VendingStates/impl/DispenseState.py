from Coin import Coin
from Item import Item

# from VendingMachineDesign import VendingMachine
from VendingStates.State import State


class DispenseState(State):
    def __init__(self, machine, code_number: int) -> None:
        print("Currently Vending machine is in DispenseState")
        self.dispense_product(machine, code_number)
    
    def click_on_insert_coin_button(self, machine):
        raise Exception("you can not click on insert coin button in Dispense state")

    def insert_coin(self, machine, coin: Coin):
        raise Exception("you can not insert Coin in Dispense state")

    def click_on_start_product_selection_button(self, machine):
        raise Exception("Product selection button cannot be clicked in Dispense state")

    def choose_product(self, machine, code_number: int):
        raise Exception("Product cannot be chosen in Dispense state")

    def get_change(self, return_change_money: int) -> int:
        raise Exception("Change cannot be returned in Dispense state")

    def dispense_product(self, machine, code_number: int) -> Item:
        from VendingStates.impl.IdleState import IdleState
        print("Product has been dispensed")
        item = machine.get_inventory().get_item(code_number)
        machine.get_inventory().update_sold_out_item(code_number)
        machine.set_vending_machine_state(IdleState(machine))
        return item

    def refund_full_money(self, machine) -> list[Coin]:
        raise Exception("Refund cannot happen in Dispense state")

    def update_inventory(self, machine, code_number, item: Item):
        raise Exception("You cannot update inventory in Selection state")
        