"""
Simulateur du bras robotique.
Objectif : trouver les angles des servomoteurs pour atteindre un objet à une distance x,y et la pince du bras dans un angle t.

todo :
- [ ] fix la fonction cercle qui marche pas
- [ ] ajouter gestion erreur dans math du bras pour pas que programme plante
- [ ] corriger erreur maths du bras
- [ ] choix du mode de focntionnement : pilotage angle, pilotage position pince, attraper objet solo.
- [ ] clean my controller : controne only la manette
"""

import askFor
import MyControler
import MyVirtualArm
import MyDraw
import MyDisplay
from time import sleep


def main():

    # Création d'un objet RobotArm
    myArm = MyVirtualArm.MyVirtualArm([0, 45, 45, 45], [50.0, 80.0, 60.0, 20.0])

    # Boucle principale
    # Affiche un menu pour choisir la simulation à effectuer
    isEnd = False
    while isEnd == False:

        print("\nQue  souhaitez voue faire : ")
        print(
            "0. Quitter."
            "\n1. Lancer une démo du bras en simulation."
            "\n2. Piloter le bras en simulation avec une manette Xbox."
            "\n3. Piloter le bras avec une manette Xbox."
            "\n4. Tester la manette Xbox."
            "\n5. Demander au bras d'attraper un objet tout seul."
        )

        choix = askFor.ABoundedNumber("Choix : ", 0, 9)

        if choix == 0:
            isEnd = True

        # Lancer une démo du bras en simulation.
        elif choix == 1:
            chooseSimulation(myArm)

        # Piloter le bras en simulation avec une manette Xbox.
        elif choix == 2:
            MyControler.controlArmInSimulationWithXboxControler(myArm)

        # Piloter le bras avec une manette Xbox.
        elif choix == 3:
            MyControler.controlArmWithXboxControler(myArm)

        # Tester la manette Xbox.
        elif choix == 4:
            MyControler.testXboxControler()

        # Demander au bras d'attraper un objet tout seul.
        elif choix == 5:
            # grabObject(myRoboticArm)
            pass

    print("Fin du programme.")


def chooseSimulation(myArm):
    isEnd = False
    while isEnd == False:
        print("\nQue voulez-vous faire : ")
        print(
            "0. Retour."
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
            # Création d'une fenêtre d'un certaine taille.
            MyDisplay.createWindow((6, 6))
            # Calcul des coordonnées des points du bras pour pouvoir les afficher.
            myArm.calculCoordonne()
            # Affichage des segments du bras.
            MyDisplay.showArmInWindow(myArm)

        # Atteindre un point avec la pince.
        elif choix == 2:
            MyDisplay.createWindow((6, 6))
            x = askFor.ABoundedNumber("x : ", myArm.xRangeMin, myArm.xRangeMax)
            y = askFor.ABoundedNumber("y : ", myArm.yRangeMin, myArm.yRangeMax)
            myArm.calculAngle([x, y])  # Calcul des angles pour atteindre le point x,y
            myArm.calculCoordonne()  # Calcul des coordonnées des points du bras pour pouvoir les afficher
            MyDisplay.showArmInWindow(myArm)

        # Atteindre un point avec la pince en affichant le mouvement.
        elif choix == 3:
            MyDisplay.createWindow((6, 6))
            xStart = askFor.ABoundedNumber(
                "xStart : ", myArm.xRangeMin, myArm.xRangeMax
            )
            yStart = askFor.ABoundedNumber(
                "yStart : ", myArm.yRangeMin, myArm.yRangeMax
            )
            xEnd = askFor.ABoundedNumber("xEnd : ", myArm.xRangeMin, myArm.xRangeMax)
            yEnd = askFor.ABoundedNumber("yEnd : ", myArm.yRangeMin, myArm.yRangeMax)
            myArm.moovePinceToCoordonate([xStart, yStart], [xEnd, yEnd], True)
            sleep(2)
            MyDisplay.closeWindow()

        # Dessiner un carré.
        elif choix == 4:
            MyDraw.drawASquare(myArm)

        # Dessiner un triangle.
        elif choix == 5:
            MyDraw.drawATriangle(myArm)

        # Dessiner un cercle.
        elif choix == 6:
            MyDraw.drawACircle(myArm)

        # Parcourir la table.
        elif choix == 7:
            MyDraw.drawAline(myArm, 1)


if __name__ == "__main__":
    main()
