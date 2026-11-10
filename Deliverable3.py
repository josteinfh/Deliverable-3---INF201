
import random

class Dice:

    def __init__(self, sides: int = 6) -> None:
        """Initialise the dice 
            Args: 
            Number of sides 
        """
        if sides < 2: 
            raise ValueError('Die must have at least 2 sides')
        self.sides = sides 


    def roll(self):
        """ Roll method for rolling dice"""
        dice_roll = random.randint(1, self.sides)
        return dice_roll

    def __repr__(self) -> str:
        return f"Dice(sides = {self.sides})"

    def __call__(self) -> int:
        """ Method allowing individual objects to be called like functions"""
        return self.roll()


    