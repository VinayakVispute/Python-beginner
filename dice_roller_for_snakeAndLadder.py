# Dice Roller for Snake and Ladder Game
# Rolls two dices
import random


class Dice_Roll:
    def roll(self):
        numbers=(random.randint(1,6),random.randint(1,6))
        return numbers


chance1=Dice_Roll()
print(chance1.roll())


