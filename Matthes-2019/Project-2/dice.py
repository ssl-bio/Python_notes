from random import randint


class Dice():
    """Documentation for Dice

    """
    def __init__(self, sides=6):
        # super(Dice, self).__init__()
        self.sides = sides

    def roll_dice(self):
        return randint(1, self.sides)
