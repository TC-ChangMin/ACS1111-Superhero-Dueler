import random

from ability import Ability
from armor import Armor
from weapon import Weapon

class Hero:
    def __init__(self, name: str, starting_health: int =100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

        self.kills: int = 0
        self.deaths: int = 0
        self.armors: list = list()
        self.abilities: list = list()

    def add_kill(self):
        self.kills += 1

    def add_death(self):
        self.deaths += 1

    def is_alive(self):
        """
        return True or False depending on whether the hero is alive or not
        """
        if self.current_health <= 0:
            print(f"{self.name} has fainted!")
            return False
        else:
            return True

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

    def fight(self, opponent):
        """
        current hero will take turns fighting the oppenent hero passed in
        """
        while self.is_alive() == True and opponent.is_alive() == True:
            self.take_damage(opponent.attack())
            opponent.take_damage(self.attack())
            print(f"{self.name} has {self.current_health} hp and {opponent.name} has {opponent.current_health} hp")

        if opponent.is_alive() == False:
            self.add_kill()
            opponent.add_death()
            print(f"{self.name} won!")

        if self.is_alive() == False:
            opponent.add_kill()
            self.add_death()
            print(f"{opponent.name} won!")
    

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero1 = Hero("wonder woman")
    hero2 = Hero("dumbledore")
    ability1 = Ability("super speed", 300)
    ability2 = Ability("super eyes", 130)
    ability3 = Ability("wizard wand", 80)
    ability4 = Ability("wizard beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)

    print(f"Hero1 deaths: {hero1.deaths}")
    print(f"Hero1 kills: {hero1.kills}")
    print("="*60)
    print(f"Hero2 deaths: {hero2.deaths}")
    print(f"Hero2 kills: {hero2.kills}")