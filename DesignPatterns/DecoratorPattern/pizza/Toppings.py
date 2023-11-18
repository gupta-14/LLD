from pizza.BasePizza import BasePizza
from pizza.ToppingDecorator import ToppingDecorator

class ExtraCheese(ToppingDecorator):
    costExtraCheese = 30
    def __init__(self, basePizza : BasePizza ):
        self.basePizza = basePizza

    def cost(self):
        return self.basePizza.cost() + self.costExtraCheese
    
class Mushroom(ToppingDecorator):
    costMushroom = 10
    def __init__(self, basePizza : BasePizza ):
        self.basePizza = basePizza

    def cost(self):
        return self.basePizza.cost() + self.costMushroom
    