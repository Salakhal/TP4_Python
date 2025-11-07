class Animal:
    def parler(self):
        raise NotImplementedError("Cette méthode doit être redéfinie")

class Chien(Animal):
    def parler(self):
        return "Ouaf !"

class Chat(Animal):
    def parler(self):
        return "Miaou !"

class Vache(Animal):
    def parler(self):
        return "Meuh !"

class Robot:
    def parler(self):
        return "Bip bop !"

def faire_parler(entite):
    print(entite.parler())

animaux_ou_robots = [Chien(), Chat(), Vache(), Robot(), Chien()]

for a in animaux_ou_robots:
    faire_parler(a)
