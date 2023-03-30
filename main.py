
import random
import degonsdragon

GUERRIER_VIE_MAX = 5
GUERRIER_DEGATS = 3
TROLL_VIE_MAX = 10
TROLL_DEGATS = 2

def attaquer_guerrier():
    return random.randint(1, GUERRIER_DEGATS)


def attaquer_troll():
    return random.randint(1, TROLL_DEGATS)


def creer_vague(niveau):
    trolls = []
    for i in range(niveau):
        vie = TROLL_VIE_MAX + (niveau - 1) * 2
        degats = TROLL_DEGATS + (niveau - 1)
        trolls.append({'vie': vie, 'degats': degats})
    return trolls

def choisir_troll(trolls):
    print("Choisissez un troll à attaquer :")
    for i, troll in enumerate(trolls):
        print(f"{i+1} : Troll avec {troll['vie']} points de vie et {troll['degats']} points de dégâts")
    choix = input("Entrez le numéro du troll que vous voulez attaquer : ")
    return trolls[int(choix)-1]




print("Choisissez votre héros :")
print("1 : Guerrier")
print("2 : Archer")
print("3 : Mage")
heros = input("Entrez le numéro de votre héros : ")
if heros == "1":
    nom_heros = "Guerrier"
    vie_heros = GUERRIER_VIE_MAX
    degats_heros = GUERRIER_DEGATS
elif heros == "2":
    nom_heros = "Archer"
    vie_heros = 4
    degats_heros = 4
elif heros == "3":
    nom_heros = "Mage"
    vie_heros = 3
    degats_heros = 5
else:
    print("Héros invalide.")
    exit()


guerrier_vie = vie_heros
vague = 1
trolls = creer_vague(vague)

def mort() :
    if guerrier_vie <= 0 :
        print("le heros est mort")
    else:
        print("il reste ", guerrier_vie,"au guerrier ")
    if TROLL_VIE_MAX <= 0 :
        print("le troll est mort")



while True:
    print(f"\n\nVague {vague} - {len(trolls)} trolls restants\n\n")

    print(f"{nom_heros} : {guerrier_vie} points de vie")
    for i, troll in enumerate(trolls):
        print(f"Troll {i+1} : {troll['vie']} points de vie et {troll['degats']} points de dégâts")


    troll = choisir_troll(trolls)




    troll['vie'] -= degats_heros
    if troll['vie'] <= 0:
        trolls.remove(troll)
        if len(trolls) == 0:
            vague += 1
            trolls = creer_vague(vague)
            guerrier_vie = vie_heros
            print(f"\n\nVous avez vaincu tous les trolls de la vague {vague-1} !\n\n")
            continue


    for troll in trolls:
        guerrier_vie -= attaquer_troll()
        if guerrier_vie <= 0:
            print("\n\nVous avez été vaincu !\n\n")
            exit()