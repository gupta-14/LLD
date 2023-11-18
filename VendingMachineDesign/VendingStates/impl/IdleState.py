from VendingStates.State import State
from VendingStates.impl.HasMoneyState import HasMoneyState
# from VendingMachine import VendingMachine
from Coin import Coin
from Item import Item

class IdleState(State):
    def __init__(self, machine=None) -> None:
        print("Currently Vending Machine is in Idle State")
        if machine is not None:
            machine.set_coin_list([])
    
    def click_on_insert_coin_button(self, machine):
        machine.set_vending_machine_state(HasMoneyState())

    def insert_coin(self, machine, coin: Coin):
        raise Exception("You cannot insert a coin in idle state")

    def click_on_start_product_selection_button(self, machine):
        raise Exception("First, you need to click on the insert coin button")

    def choose_product(self, machine, code_number: int):
        raise Exception("You cannot choose a product in idle state")

    def get_change(self, return_change_money: int) -> int:
        raise Exception("You cannot get change in idle state")

    def dispense_product(self, machine, code_number: int) -> Item:
        raise Exception("You cannot get refunded in idle state")

    def refund_full_money(self, machine) -> list[Coin]:
        raise Exception("Product cannot be dispensed in idle state")

    def update_inventory(self, machine, code_number, item: Item):
        machine.get_inventory().add_item(item, code_number)
    