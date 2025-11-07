from abc import ABC, abstractmethod
import math

class ColorMixin:
    def __init__(self, couleur="blanc"):
        self.couleur = couleur

    def couleur_str(self):
        return f"Couleur : {self.couleur}"


class Forme(ABC):
    @abstractmethod
    def aire(self):
        pass

    def __str__(self):
        if isinstance(self, ColorMixin):
            return f"{self.__class__.__name__} – aire : {self.aire():.2f} – {self.couleur_str()}"
        return f"{self.__class__.__name__} – aire : {self.aire():.2f}"

class Cercle(Forme, ColorMixin):
    def __init__(self, rayon, couleur="blanc"):
        ColorMixin.__init__(self, couleur)
        self.rayon = rayon

    def aire(self):
        return math.pi * self.rayon ** 2

class Rectangle(Forme, ColorMixin):
    def __init__(self, largeur, hauteur, couleur="blanc"):
        ColorMixin.__init__(self, couleur)
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur

class Triangle(Forme, ColorMixin):
    def __init__(self, base, hauteur, couleur="blanc"):
        ColorMixin.__init__(self, couleur)
        self.base = base
        self.hauteur = hauteur

    def aire(self):
        return 0.5 * self.base * self.hauteur


class Carre(Rectangle):
    def __init__(self, cote, couleur="blanc"):
        super().__init__(cote, cote, couleur)

if __name__ == "__main__":
    formes = [
        Cercle(3, "rouge"),
        Rectangle(4, 5, "vert"),
        Triangle(6, 2, "bleu"),
        Carre(4, "jaune")
    ]

    for f in formes:
        print(f)

def tests_unitaires():
    c = Cercle(1)
    assert round(c.aire(), 2) == 3.14, "Erreur Cercle"

    r = Rectangle(2, 3)
    assert r.aire() == 6, "Erreur Rectangle"

    t = Triangle(4, 2)
    assert t.aire() == 4, "Erreur Triangle"

    car = Carre(5)
    assert car.aire() == 25, "Erreur Carré"

    print("Tous les tests unitaires sont passés !")

tests_unitaires()
