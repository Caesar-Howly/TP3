import random

play_game = True
def encounter():
    print(f"Vous tombez face à face avec un adversaire de difficulté: {force_adversaire}!")
    print("""Que voulez-vous faire?
            1- Combattre cet adversaire
            2- Contourner cet adversaire et aller ouvrir une autre porte
            3- Afficher les règles du jeu
            4- Quitter la partie""")

while play_game:
    force_adversaire = random.randint(1, 5)
    nbr_vie = 20

    encounter()