class Character:

    """Represents a character in the RPG"""
    
    def __init__(self, name: str, hp_max: int = 100, damage: int = 10, heal_up: int = 5, weapon: Weapon | None = None) -> None:
        """
        Initialise the Character
        Args:
            name (str): The name of the character.
            hp_max (int): Max hit points (default = 100)
            damage (int): Damage dealt when character attacks (default = 10)
            heal_up (int): Default healing amount (default = 5)
        """
        self.name = name
        self._hp = hp_max  # Note: _hp indicates private attribute
        self.hp_max = hp_max
        self.damage = damage
        self.heal_up = heal_up
        self.weapon = weapon

    @property
    def is_alive(self) -> bool:
        """Check if the character is still alive"""
        return self._hp > 0

    def attack(self, target) -> None:
        """Attack and deal damage to target character"""
        if self.weapon is not None:
            weapon_damage = self.weapon.roll_damage()
            target.take_damage(weapon_damage)
        else:
            target.take_damage(self.damage)

    def take_damage(self, amount: int) -> None:
        """Character takes damage"""
        self._hp -= amount
        self._hp = max(self._hp, 0)

    def heal(self, amount: int = None) -> None:
        """Heal the character"""
        heal_amount = amount if amount is not None else self.heal_up
        self._hp += heal_amount
        self._hp = min(self._hp, self.hp_max)  # HP cannot exceed max HP

    def introduce(self) -> None:
        """Creates string that introduces character"""
        print(f"Hi, my name is {self.name}!")

    def __repr__(self) -> str:
        """Representation of character object"""
        return f"<Character name={self.name} hp={self.hp} damage={self.damage}>"

    def __str__(self) -> str:
        """String representation of character object"""
        return f"Character: {self.name} with {self.hp} HP and {self.damage} damage"

    @property
    def hp(self) -> int:
        """Public read-only property to inspect HP without allowing direct, unsafe modification"""
        return self._hp



class Warrior(Character):
    def __init__(self, name, hp_max = 100, damage = 10, heal_up = 5, armor: int = 5, weapon = None):
        super().__init__(name, hp_max, damage, heal_up, weapon)
        self.armor = armor

    def take_damage(self, amount: int) -> None:
        reduced_damage = max(amount-self.armor, 1)
        super().take_damage(reduced_damage)


class Mage(Character):
    def __init__(self, name, hp_max = 100, damage = 10, heal_up = 5, weapon = None, mana: int = 30, mana_max: int =30):
        super().__init__(name, hp_max, damage, heal_up, weapon)
        self.mana = mana 
        self.mana_max = mana_max

    def attack(self, target):
        if self.mana >= 10:
            self.mana -= 10
            spell_damage = self.damage*2
            target.take_damage(spell_damage)
        else:
            self.mana = min(self.mana += 5, mana_max)
            mana = max(mana, 30)
            super().attack(target)

