import random

from ability import Ability
from armor import Armor
from weapon import Weapon

class Hero:
    def __init__(self, name: str, starting_health: int =100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

        self.armors: list = list()
        self.abilities: list = list()

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage
    
    def add_weapon(self, weapon):
        self.abilities.append(weapon)
    
    def add_armor(self, armor):
        self.armors.append(armor)

    def defend(self):
        total_blocked = 0
        for blocked_damage in self.armors:
            total_blocked += blocked_damage.block()
        return total_blocked
    
    def take_damage(self, damage):
        damage_taken = damage - self.defend() 
        self.current_health -= damage_taken
        return self.current_health

    """def fight(self, opponent):
      winner = random.choice([self, opponent])
      return f"{winner.name} wins!"
    """

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())