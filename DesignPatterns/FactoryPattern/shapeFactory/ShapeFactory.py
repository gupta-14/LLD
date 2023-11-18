from shapeFactory.Circle import Circle
from shapeFactory.Rectangle import Rectangle

class ShapeFactory:
    def __init__(self, input) -> None:
        self.input = input

    def getShape(self):
        if self.input == "CIRCLE":
            return Circle()
        
        elif self.input == "RECTANGLE":
            return Rectangle()

        else:
            return None