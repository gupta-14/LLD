from pizza.RegularPizza import Margherita, VegDelight
from pizza.Toppings import ExtraCheese, Mushroom

pizza1 = ExtraCheese(Margherita()).cost()
pizza2 = Mushroom(ExtraCheese(VegDelight())).cost()
print(pizza1, pizza2)