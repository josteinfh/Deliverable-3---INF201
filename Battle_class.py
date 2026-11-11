

class Battle():
    """Create a class for battles between heros and enemies"""
    def __init__(self, hero: Character, enemy: Character):
        self.hero = hero 
        self.enemy = enemy 

    def play_round(self) -> None:
        """Method that implements combat logic"""
        self.hero.attack(self.enemy)
        if self.enemy.is_alive:
            self.enemy.attack(self.hero)


    def simulate_battle(self) -> None:
        """Method that simulates a complete battle"""
        while self.hero.is_alive and self.enemy.is_alive:
            self.play_round() 

