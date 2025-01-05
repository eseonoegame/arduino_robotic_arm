"""
Simulateur du bras robotique.
Objectif : trouver les angles des servomoteurs pour atteindre un objet à une distance x,y et la pince du bras dans un angle t.

todo :
- [ ] fix la fonction cercle qui marche pas
- [ ] ajouter gestion erreur dans math du bras pour pas que programme plante
- [ ] corriger erreur maths du bras
- [ ] dissocier la simulation du bras
- [ ] choix du mode de focntionnement : pilotage angle, pilotage position pince, attraper objet solo.
- [ ] clean my controller : controne only la manette"""

import askFor as askFor
from MyVirtualArm import *
from MySimulation import *
from MyControler import *
from MyCom import *

def main():
    
    # Création d'un objet RobotArm
    myArm = MyVirtualArm([0, 45, 45, 45],[50.0, 80.0, 60.0, 20.0])

    isEnd = False
    
    # Boucle principale
    # Affiche un menu pour choisir la simulation à effectuer
    while isEnd == False:
        
        print("\nQue  souhaitez voue faire : ")
        print("0. Quitter."
              "\n1. Lancer une démo du bras en simulation."
              "\n2. Piloter le bras en simulation avec une manette Xbox."
              "\n3. Piloter le bras avec une manette Xbox."
              "\n4. Tester la manette Xbox."
              "\n5. Demander au bras d'attraper un objet tout seul.")

        
        choix = askFor.ABoundedNumber("Choix : ", 0, 9)

        if choix == 0: 
            isEnd = True

        # Lancer une démo du bras en simulation.
        elif choix == 1:
            chooseSimulation(myArm)
        
        # Piloter le bras en simulation avec une manette Xbox."
        elif choix == 2:
            controlArmInSimulationWithXboxControler(myArm)
            pass
        
        # Piloter le bras avec une manette Xbox.
        elif choix == 3 :
            controlArmWithXboxControler(myArm)
            pass

        # Tester la manette Xbox.
        elif choix == 4:
            testXboxControler()
            pass

        # Demander au bras d'attraper un objet tout seul.
        elif choix == 5:
            #grabObject(myRoboticArm)
            pass


if __name__ == "__main__":
    main()