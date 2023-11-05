import random

class Dice:

    def __init__(self, diceCount) -> None:
        self.diceCount = diceCount
        self.mini = 1
        self.maxi = 6
    
    def rollDice(self):
        totalSum = 0
        diceUsed = 0
        while diceUsed<self.diceCount:
            totalSum += random.randint(self.mini, self.maxi)
            diceUsed += 1
        return totalSum
    