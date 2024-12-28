"""
Simulateur du bras robotique.
Objectif : trouver les angles des servomoteurs pour atteindre un objet à une distance x,y et la pince du bras dans un angle t.
"""

import askFor as askFor
import console as console
import matplotlib.pyplot as plt
from math import *
from robot import RobotArm

def simulateur():
    
    # Création d'un objet RobotArm
    arm = RobotArm([0, 45, 45, 45],[50, 80, 60, 20])

    isEnd = False
    
    # Boucle principale
    # Affiche un menu pour choisir la simulation à effectuer
    while isEnd == False:
        
        print("\nAffichage des segments du bras robot : ")
        print("0. Quitter."
              "\n1. pour des angles par défaut."
              "\n2. pour la pince sur un objet à une distance x,y donnée."
              "\n3. pour la pince sur un objet à une distance x variant entre xmin et xmax."
              "\n4. pour bouger d'une position à une autre."
              "\n5. démo soutenance table.")
        
        choix = askFor.ABoundedNumber("Choix : ", 0, 5)

        if choix == 0: 
            isEnd = True

        elif choix == 1:
            plt.figure(figsize=(9, 9))  # Création d'une fenêtre d'un certaine taille
            arm.calculCoordonne()       # Calcul des coordonnées des points du bras pour pouvoir les afficher
            arm.show()                  # Affichage des segments du bras
            arm.showAngles()            # Affichage des angles des servomoteurs
        
        elif choix == 2:
            plt.figure(figsize=(9, 9))
            x = askFor.ABoundedNumber("x : ", arm.xRangeMin, arm.xRangeMax)
            y = askFor.ABoundedNumber("y : ", arm.yRangeMin, arm.yRangeMax)
            arm.calculAngle([x,y])       # Calcul des angles pour atteindre le point x,y
            arm.calculCoordonne()        # Calcul des coordonnées des points du bras pour pouvoir les afficher 
            arm.show()                   # Affichage des segments du bras

        elif choix == 3:
            plt.figure(figsize=(9, 9))
            xStart = 20
            yStart = 0
            xEnd = 90
            yEnd = 0
            arm.moovePinceToCoordonate([xStart,yStart],[xEnd,yEnd],True) # Bouger la pince d'un point à un autre
        
        elif choix == 4:
            plt.figure(figsize=(9, 9))
            xStart = askFor.ABoundedNumber("xStart : ", arm.xRangeMin, arm.xRangeMax)
            yStart = askFor.ABoundedNumber("yStart : ", arm.yRangeMin, arm.yRangeMax)
            xEnd = askFor.ABoundedNumber("xEnd : ", arm.xRangeMin, arm.xRangeMax)
            yEnd = askFor.ABoundedNumber("yEnd : ", arm.yRangeMin, arm.yRangeMax)
            arm.moovePinceToCoordonate([xStart,yStart],[xEnd,yEnd],True)

        elif choix == 5:
            plt.figure(figsize=(9, 9))
            while True:    
                xStart = 50
                yStart = 30
                xEnd = 120
                yEnd = 30
                arm.moovePinceToCoordonate([xStart,yStart],[xEnd,yEnd],True)
                arm.moovePinceToCoordonate([xEnd,yEnd],[xStart,yStart],True)
                

if __name__ == "__main__":
    simulateur()