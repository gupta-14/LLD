from ItemType import ItemType

class Item:
    def __init__(self) -> None:
        self.type: ItemType = None
        self.price: int = None

    def get_type(self):
        return self.type

    def set_type(self, item_type):
        self.type = item_type

    def get_price(self):
        return self.price
    
    def set_price(self, price):
        self.price = price