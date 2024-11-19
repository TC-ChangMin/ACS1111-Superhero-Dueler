from hero import Hero


class Team():
    def __init__(self, name: str):
        self.name = name

        self.heroes = []

    def add_hero(self, hero):
        self.heroes.append(hero)

    def remove_hero(self, name):
        foundHero = False
        # loop through each hero in our list
        for hero in self.heroes:
        # if we find them, remove them from the list
            if hero.name == name:
                self.heroes.remove(hero)
                foundHero = True
        if not foundHero:
            return 0
        
    def view_all_heroes(self):
        if len(self.heroes) > 0:
            for hero in self.heroes:
                print(hero.name)
        else:
            return "No heroes Found"