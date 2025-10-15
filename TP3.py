import random

nbr_combat = 0
nbr_vie = 20
play_game = True
boss = 0


def force_personnage(low, high):
    return random.randint(low, high)

regles = False
force_adversaire = 0

while play_game:

    nbr_combat += 1
    if not regles:
        if boss != 0 and boss % 3 == 0:
            force_adversaire = force_personnage(5, 10)
            print(f"Il y a un monstre incroyablement fort de force {force_adversaire}")

        else:
            force_adversaire = force_personnage(1, 5)
            print(f"Vous tombez face à face avec un adversaire de difficulté: {force_adversaire}!")
        regles = False
    else:
        print(f"Vous tombez face à face avec un adversaire de difficulté: {force_adversaire}!")

    choix = str(input("""Que voulez-vous faire?
            1- Combattre cet adversaire
            2- Contourner cet adversaire et aller ouvrir une autre porte
            3- Afficher les règles du jeu
            4- Quitter la partie"""))

    if choix == "1":
        force_joueur = random.randint(1, 6)
        print(f"Vous avez la force de {force_joueur}.")
        if force_joueur <= force_adversaire:
            print(f"Oh, non! Vous avez perdu.")
            nbr_vie -= force_adversaire
            print(f"Vous avez désormais {nbr_vie} points de vie.")
        else:
            print("Woohoo! Vous avez battu le monstre.")
            nbr_vie += force_adversaire
            print(f"Vous avez désormais {nbr_vie} points de vie.")
            boss += 1

    elif choix == "2":
        print("Vous fermez la porte avant que le monstre puisse te prendre, mais il te gratte.")
        nbr_vie -= 1
        print(f"Vous avez désormais {nbr_vie} points de vie.")

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
        malice du monstre. Il te prend par le cou et l'air est coupé de ton corps. Il te regarde avec un sourire qui 
        te montre ses dents pointus. Tu cries avec tout ta force pendant que tu rentre dans sa bouche et...
        """)

        print("Aw... Vous avez perdu. À bientôt..!")
        play_game = False

    if nbr_vie <= 0:
        print("Whoops! Vous n'avez plus de points de vie. Vous avez perdu. À bientôt!")
        play_game = False


nbr_vie = 20
