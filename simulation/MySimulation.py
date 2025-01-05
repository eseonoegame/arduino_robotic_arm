import askFor as askFor
import matplotlib.pyplot as plt
from math import *

def chooseSimulation(myArm): 
    isEnd = False
    while isEnd == False:
        print("\nQue voulez-vous faire : ")
        print("0. Quitter."
                "\n1. Afficher le bras."
                "\n2. Atteindre un point avec la pince."
                "\n3. Atteindre un point avec la pince en affichant le mouvement."
                "\n4. Dessiner un carré."
                "\n5. Dessiner un triangle."
                "\n6. Dessiner un cercle."
                "\n7. Parcourir la table."
                )
        choix = askFor.ABoundedNumber("Choix : ", 0, 9)    
        
        if choix == 0:
            isEnd = True

        # Afficher le bras.
        elif choix == 1:
            plt.figure(figsize=(6, 6))  # Création d'une fenêtre d'un certaine taille
            myArm.calculCoordonne()       # Calcul des coordonnées des points du bras pour pouvoir les afficher
            myArm.show()                  # Affichage des segments du bras
            myArm.showAngles()            # Affichage des angles des servomoteurs

        # Atteindre un point avec la pince.
        elif choix == 2:
            plt.figure(figsize=(6, 6))
            x = askFor.ABoundedNumber("x : ", myArm.xRangeMin, myArm.xRangeMax)
            y = askFor.ABoundedNumber("y : ", myArm.yRangeMin, myArm.yRangeMax)
            myArm.calculAngle([x,y])       # Calcul des angles pour atteindre le point x,y
            myArm.calculCoordonne()        # Calcul des coordonnées des points du bras pour pouvoir les afficher 
            myArm.show()                   # Affichage des segments du bras

        # Atteindre un point avec la pince en affichant le mouvement.
        elif choix == 3:
            plt.figure(figsize=(6, 6))
            xStart = askFor.ABoundedNumber("xStart : ", myArm.xRangeMin, myArm.xRangeMax)
            yStart = askFor.ABoundedNumber("yStart : ", myArm.yRangeMin, myArm.yRangeMax)
            xEnd = askFor.ABoundedNumber("xEnd : ", myArm.xRangeMin, myArm.xRangeMax)
            yEnd = askFor.ABoundedNumber("yEnd : ", myArm.yRangeMin, myArm.yRangeMax)
            myArm.moovePinceToCoordonate([xStart,yStart],[xEnd,yEnd],True)

        # Dessiner un carré.
        elif choix == 4:
            plt.figure(figsize=(6, 6))
            for _ in range(2):    
                x1 = 75
                y1 = 50

                x2 = 125
                y2 = 50

                x3 = 125
                y3 = 100

                x4 = 75
                y4 = 100

                myArm.moovePinceToCoordonate([x1,y1],[x2,y2],True)
                myArm.moovePinceToCoordonate([x2,y2],[x3,y3],True)
                myArm.moovePinceToCoordonate([x3,y3],[x4,y4],True)
                myArm.moovePinceToCoordonate([x4,y4],[x1,y1],True)

        # Dessiner un triangle.
        elif choix == 5:
            plt.figure(figsize=(6, 6))

            x1 = 50
            y1 = 50

            x2 = 100
            y2 = 50

            x3 = 100
            y3 = 100

            myArm.moovePinceToCoordonate([x1,y1],[x2,y2],True)
            myArm.moovePinceToCoordonate([x2,y2],[x3,y3],True)
            myArm.moovePinceToCoordonate([x3,y3],[x1,y1],True)


        # Dessiner un cercle.
        elif choix == 6:
            plt.figure(figsize=(6, 6))
            x = 75
            y = 75
            r = 25
            for i in range(0, 618, 10): # 628 = 2*pi*100
                i = i/100
                x1 = round (x + r * cos(i))
                y1 = round (y + r * sin(i))
                x2 = round (x + r * cos(i+0.1)) 
                y2 = round (y + r * sin(i+0.1))
                myArm.moovePinceToCoordonate([x1,y1],[x2,y2],True)

        # Parcourir la table.
        elif choix == 7:
            plt.figure(figsize=(6, 6))
            for _ in range(2):   
                xStart = 50
                yStart = 0
                xEnd = 120
                yEnd = 0
                myArm.moovePinceToCoordonate([xStart,yStart],[xEnd,yEnd],True)
                myArm.moovePinceToCoordonate([xEnd,yEnd],[xStart,yStart],True)


