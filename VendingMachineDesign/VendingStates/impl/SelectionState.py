from Coin import Coin
from Item import Item

# from VendingMachineDesign import VendingMachine
from VendingStates.State import State
from VendingStates.impl.DispenseState import DispenseState


class SelectionState(State):
    def __init__(self, machine) -> None:
        print("Currently Vending machine is in SelectionState")
    
    def click_on_insert_coin_button(self, machine):
        raise Exception("you can not click on insert coin button in Selection state")

    def insert_coin(self, machine, coin: Coin):
        raise Exception("you can not insert Coin in selection state")

    def click_on_start_product_selection_button(self, machine):
        return

    def choose_product(self, machine, code_number: int):
        # 1. get item of this codeNumber
        item = machine.get_inventory().get_item(code_number)

        # 2. total amount paid by User
        paid_by_user = sum(coin.value for coin in machine.get_coin_list())

        # 3. compare product price and amount paid by user
        if paid_by_user < item.get_price():
            print(f"Insufficient Amount, Product you selected is for price: {str(item.get_price())} and you paid: {str(paid_by_user)}")
            self.refund_full_money(machine)
            raise Exception("Insufficient amount")
        elif paid_by_user >= item.get_price():
            if paid_by_user > item.get_price():
                self.get_change(paid_by_user - item.get_price())
            machine.set_vending_machine_state(DispenseState(machine, code_number))

    def get_change(self, return_change_money: int) -> int:
        print(f"Returned the change in the Coin Dispense Tray: {str(return_change_money)}")
        return return_change_money

    def dispense_product(self, machine, code_number: int) -> Item:
        raise Exception("You cannot get refunded in Selection state")

    def refund_full_money(self, machine) -> list[Coin]:
        from VendingStates.impl.IdleState import IdleState
        print("Returned the full amount back in the Coin Dispense Tray")
        machine.set_vending_machine_state(IdleState(machine))
        return machine.get_coint_list()

    def update_inventory(self, machine, code_number, item: Item):
        raise Exception("You cannot update inventory in Selection state")
    