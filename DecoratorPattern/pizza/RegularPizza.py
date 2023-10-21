from pizza.BasePizza import BasePizza

class FarmHouse(BasePizza):
    def cost(self):
        return 200
    

class VegDelight(BasePizza):
    def cost(self):
        return 150
    

class Margherita(BasePizza):
    def cost(self):
        return 100
    