class Character:
    """Represents a character in the RPG"""
    
    def __init__(self, name: str, hp_max: int = 100, damage: int = 10, heal_up: int = 5) -> None:
        """
        Initialise the Character
        Args:
            name (str): The name of the character.
            hp_max (int): Max hit points (default = 100)
            damage (int): Damage dealt when character attacks (default = 10)
        """
        self.name = name
        self._hp = hp_max  # Note: _hp indicates private attribute
        self.hp_max = hp_max
        self.damage = damage
        self.heal_up = heal_up
        self.is_alive = if _hp > 0 True else False 

    def attack(self, target) -> None:
        """Attack and deal damage to target character"""
        take_damage(self, target)


    def take_damage(self, target) -> None:
        """Charachter takes damage"""
        target._hp -= self.damage
        target._hp = max(target._hp, 0)

    def heal(self, heal_up) -> None:
        """Charachter heals"""
        self.hp += heal_up
        self._hp = max(self._hp, 0)

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