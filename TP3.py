import random


global numero_adversaire
nbr_combat = 0

play_game = True


def encounter():
    global nbr_vie
    global nbr_combat
    nbr_combat += 1

    force_adversaire = random.randint(1, 5)

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

    elif choix == "2":
        print("Vous fermez la porte avant que le monstre puisse te prendre, mais il te gratte.")
        nbr_vie -= 1
        print(f"Vous avez désormais {nbr_vie} points de vie.")

    elif choix == "3":
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

        print("Aw... Vous avez perdu. À bientot..!")
        global play_game
        play_game = False


nbr_vie = 20

while play_game:

    encounter()
    