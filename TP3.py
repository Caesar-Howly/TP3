"""
Nom: Caesar Howly
Groupe: 407
Ce code crée un jeu ou le joueur cours dans une couloir et, a chaque porte, il tombe face à face avec un monstre de
force 1 à 5. Il jette donc un dé de 1 à 6. S'il recoit une nombre plus petite ou egale à la force du monstre, il perd le
même nombre de vies au nombre de la force du monstre. S'il recoit une nombre plus grande que la force du monstre, il
gagne le même nombre de vies au force du monstre. Après trois victoires,le joueur aura contre un monstre plus fort, le
boss, qui a un minimum de 5 et un maximum de 10. Le joueur recevra un dé de 1 à 11 pour pouvoir gagner. Sinon, si le
monstre et trop fort, le joueur pourra échapper le monstre en sacrifiant 1 point de vie.
"""
import random

play_game = True
nbr_combat = 0
nbr_vie = 20
boss = 0
nbr_victoire = 0
nbr_perds = 0
victoire_cons = 0


class Colors:
    RESET = '\033[0m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    BLUE = '\033[34m'
    CYAN = '\033[36m'


def force_personnage(low, high):
    return random.randint(low, high)


regles = False
force_adversaire = 0

while play_game:

    if not regles:
        if boss != 0 and boss % 3 == 0:
            force_adversaire = force_personnage(4, 5) + force_personnage(4, 5)
            print(f"Il y a un monstre incroyablement fort de force {force_adversaire}")
        else:
            force_adversaire = force_personnage(1, 5) + force_personnage(1, 5)
            print(f"Vous tombez face à face avec un adversaire de difficulté: {force_adversaire}!")
        regles = False
    else:
        if boss != 0 and boss % 3 == 0:
            print(f"Il y a un monstre incroyablement fort de force {force_adversaire}")
        else:
            print(f"Vous tombez face à face avec un adversaire de difficulté: {force_adversaire}!")

    choix = str(input("""Que voulez-vous faire?
            1- Combattre cet adversaire
            2- Contourner cet adversaire et aller ouvrir une autre porte
            3- Afficher les règles du jeu
            4- Quitter la partie
            """))

    if choix == "1":
        nbr_combat += 1
        if boss != 0 and boss % 3 == 0:
            force_joueur = force_personnage(1, 6) + force_personnage(1, 6)
            boss = 0
        else:
            force_joueur = force_personnage(1, 6) + force_personnage(1, 6)
        print(f"Vous avez la force de {force_joueur}.")
        if force_joueur <= force_adversaire:
            print(f"Oh, non! Vous avez perdu.")
            nbr_vie -= force_adversaire
            print(f"Vous avez désormais {nbr_vie} points de vie.")
            nbr_perds += 1
            victoire_cons = 0
        else:
            print("Woohoo! Vous avez battu le monstre.")
            nbr_vie += force_adversaire
            print(f"Vous avez désormais {nbr_vie} points de vie.")
            boss += 1
            nbr_victoire += 1
            victoire_cons += 1

    elif choix == "2":
        print("Vous fermez la porte avant que le monstre puisse te prendre, mais il te gratte.")
        nbr_vie -= 1
        print(f"Vous avez désormais {nbr_vie} points de vie.")
        victoire_cons = 0

    elif choix == "3":
        regles = True
        print("""
        Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.  Dans ce 
        cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.
        
        Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de 
        l’adversaire.  Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.

        La partie se termine lorsque les points de vie de l’usager tombent sous 0.

        L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point 
        de vie.
        """)

    else:
        print("""Vous regardez le monstre pendant qu'il cours vers toi. Vous restez ancré sur le sol, effrayez de la 
        malice du monstre. Il te prend par le cou. Tu ne peux pas respirer. Il te regarde avec une sourire qui 
        te montre ses dents pointus. Tu cries avec tout ta force pendant que tu rentre dans sa bouche et...
        """)

        print("Aw, vous avez perdu. À bientôt!")
        play_game = False

    if nbr_vie <= 0:
        print("Whoops! Vous n'avez plus de points de vie. Vous avez perdu.")
        rejouer = str(input("Voulez-vous recommencer? o/n"))
        if rejouer == "o":
            print("On y va!")
            nbr_vie = 20
            nbr_combat = 0
            nbr_victoire = 0
            nbr_perds = 0
        else:
            print("Au revoir.")
            play_game = False

    print(Colors.CYAN + f"Vous avez combattu {nbr_combat} fois." + Colors.RESET)
        
    print(Colors.BLUE + f"Vous avez gagnez {nbr_victoire} fois" + Colors.RESET)

    print(Colors.RED + f"Vous avez perdu {nbr_perds} fois." + Colors.RESET)

    print(Colors.GREEN + f"Vous avez gagnez {victoire_cons} fois consécutivement." + Colors.RESET)
