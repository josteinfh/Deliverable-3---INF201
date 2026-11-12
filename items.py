from Die_class import Dice

class Weapon:
    def __init__(self, name: str, damage_dice: Dice) -> None:
        """Intialising the weapon class
        2 attributes: name and damage_dice"""

        self.name = name 
        self.damage_dice = damage_dice


    def roll_damage(self) -> int:
        return self.damage_dice.roll()