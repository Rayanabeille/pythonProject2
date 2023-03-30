from random import *
guerrier_degat = 5
guerrier_vie = 10
troll_vie = 5
troll_degat = 5


class Actor:
    def __init__(self, name, life_points, weapon_points):
        self.name = name
        self.life_points = life_points
        self.weapon_points = weapon_points

    def fight(self, actor):
        print(self.name, "attacks", actor.name, "...")
        actor.life_points -= random.randint(1, self.weapon_points)

    def isDead(self):
        return self.life_points <= 0;

def attaquer_guerrier():
    return random.randint(1, guerrier_degat)

def attaquer_troll():
    return random.randint(1, troll_degat)

def mort() :
    if guerrier_vie <= 0 :
        print("le heros est mort")
    else:
        print("il reste ", guerrier_vie,"au guerrier ")
    if troll_vie <= 0 :
        print("le troll est mort")



while guerrier_vie > 0 and troll_vie > 0:
    print("Le guerrier attaque le troll !")
    troll_vie -= attaquer_guerrier()
    print("Le troll a maintenant", troll_vie, "points de vie.")

    if troll_vie <= 0:
        print("Le guerrier a vaincu le troll ")
        break

    print("Le troll attaque le guerrier ")
    guerrier_vie -= attaquer_troll()
    print("Le guerrier a maintenant", guerrier_vie, "points de vie.")