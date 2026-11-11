

class Weapon:
    def __init__(self, name: str, damage_dice: Dice):
        """Intialising the weapon class
        2 attributes: name and damage_dice"""

        self.name = name 
        self.damage_dice = damage_dice


    def roll_damage(self):
        return self.damage_dice.roll()