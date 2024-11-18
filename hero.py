import random

class Hero:
    def __init__(self, name: str, starting_health: int =100):
       if not isinstance(name, str):
           raise ValueError("name must be a string")
       if not isinstance(starting_health, int):
           raise ValueError("health must be an integer")

    def fight(self, opponent):
      winner = random.choice([self, opponent])
      return f"{winner.name} wins!"

if __name__ == "__main__":
   hero1 = Hero("Wonder Woman")
   hero2 = Hero("Dumbledore")

   print(hero1.fight(hero2))