from Item import Item

class ItemShelf:
    def __init__(self) -> None:
        self.code = None
        self.item = None
        self.sold_out = False

    def get_code(self) -> int:
        return self.code

    def set_code(self, code: int) -> None:
        self.code = code

    def get_item(self) -> Item:
        return self.item

    def set_item(self, item: Item) -> None:
        self.item = item

    def is_sold_out(self) -> bool:
        return self.sold_out

    def set_sold_out(self, sold_out: bool) -> None:
        self.sold_out = sold_out
