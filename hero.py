import random

class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def fight(self, opponent):
      winner = random.choice([self, opponent])
      return f"{winner.name} wins!"

if __name__ == "__main__":
   hero1 = Hero("Wonder Woman")
   hero2 = Hero("Dumbledore")

   print(hero1.fight(hero2))