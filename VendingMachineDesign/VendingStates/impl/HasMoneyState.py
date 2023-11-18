
from Coin import Coin
from Item import Item

# from VendingMachineDesign import VendingMachine
from VendingStates.State import State
from VendingStates.impl.SelectionState import SelectionState

class HasMoneyState(State):
    def __init__(self, machine) -> None:
        print("Currently Vending machine is in HasMoneyState")
    
    def click_on_insert_coin_button(self, machine):
        return

    def insert_coin(self, machine, coin: Coin):
        print("Accepted the coin")
        machine.get_coin_list().append(coin)

    def click_on_start_product_selection_button(self, machine):
        machine.set_vending_machine_state(SelectionState())

    def choose_product(self, machine, code_number: int):
        raise Exception("You need to click on the start product selection button first")

    def get_change(self, return_change_money: int) -> int:
        raise Exception("You cannot get change in HasMoney state")

    def dispense_product(self, machine, code_number: int) -> Item:
        raise Exception("You cannot get refunded in HasMoney state")

    def refund_full_money(self, machine) -> list[Coin]:
        from VendingStates.impl.IdleState import IdleState
        print("Returned the full amount back in the Coin Dispense Tray")
        machine.set_vending_machine_state(IdleState(machine))
        return machine.get_coint_list()

    def update_inventory(self, machine, code_number, item: Item):
        raise Exception("You cannot update inventory in HasMoney state")
    