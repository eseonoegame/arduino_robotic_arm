# Noé Game E2

def tabDisplay(tab,largeur):
    """Affiche un tableau avec des colonnes de même largeur."""
    for i in range(len(tab)):
        ligne = ""
        for j in range(len(tab[i])):
            n = len(str(tab[i][j]))
            gap = largeur-n
            ligne = ligne + str(tab[i][j]) + " "*gap
        print(ligne)


