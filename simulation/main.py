"""
Simulateur du bras robotique.
Objectif : trouver les angles des servomoteurs pour atteindre un objet à une distance x,y et la pince du bras dans un angle t.
"""

import askFor as askFor
import console as console
import matplotlib.pyplot as plt
from math import *

# --- Classes ---
class Target :
    def __init__(self,x,y,t):
        self.x = x
        self.y = y
        self.t = t 

    def __str__(self):
        return (f"Position de l'objet : ({self.x},{self.y})"
                "\nAngle d'approche : {self.t}")

    def show(self):
        """Dessine l'objet à attraper."""
        plt.plot(self.x, self.y, 'ro')
        plt.pause(0.05)
        plt.show()

class RobotArm :
    def __init__(self,A,B):
        """ 
        Angle par défaut du bras robot. 
        Longueur des segments du bras robot.
        """
        self.A = A
        self.B = B

        self.xRangeMax = sum(B)-B[0]
        self.xRangeMin = 0
        self.yRangeMax = sum(B)-B[0]
        self.yRangeMin = 0

        self.A = degreeToRadian(A)
        self.Sx = [0, 0, 0, 0, 0]
        self.Sy = [0, 0, 0, 0, 0]

    def __str__(self):
        return (f"Longueur des segments : {self.B}"
                "\nAngles des servomoteurs : {self.A}")

    def showAngles(self):
        """ Affiche les angles du bras robot. """
        liste = []
        largeur = 15

        for i in range(len(self.A)):
            liste.append([f"Angle {i} : ",f"{round(degrees(self.A[i]),3)} deg", f"{round(self.A[i],3)} rad"])
        
        print("\n" + largeur*3*"-")
        console.tabDisplay(liste, largeur)
        print(largeur*3*"-"+ "\n")

    def show(self):
        """Dessine le bras robotique."""
        Sx,Sy = self.calculCoordonne()
        for i in range(len(Sx)-1):
            plt.plot([Sx[i], Sx[i+1]], [Sy[i], Sy[i+1]], label=f"B{i}")
        plt.pause(0.05)
        plt.draw()

    def calculCoordonne(self):
        """ 
        Calcul les coordonnées des points du bras robot.
        Paramètres : Les angles et les longueurs des segments du bras.
        Retourne : Les coordonnées des points des segments du bras.
        """

        A = self.A
        B = self.B
        Sx = self.Sx
        Sy = self.Sy

        Sx,Sy = [],[]
        for i in range(len(A)+1):
            Sx.append(0)
            Sy.append(0)

        Sx[0] = 0
        Sy[0] = 0

        Sx[1] = Sx[0] + B[0]*sin(A[0])
        Sy[1] = Sy[0] + B[0]*cos(A[0])

        Sx[2] = Sx[1] + B[1]*sin(A[0]+A[1])
        Sy[2] = Sy[1] + B[1]*cos(A[0]+A[1])

        Sx[3] = Sx[2] + B[2]*sin(A[0]+A[1]+A[2])
        Sy[3] = Sy[2] + B[2]*cos(A[0]+A[1]+A[2])

        Sx[4] = Sx[3] + B[3]*sin(A[0]+A[1]+A[2]+A[3])
        Sy[4] = Sy[3] + B[3]*cos(A[0]+A[1]+A[2]+A[3])

        return Sx, Sy

    def calculAngle(self, target):
        """ 
        Calcule les angles du bras robot pour atteindre un point (x,y) avec une pince dans un angle t. 
        """

        B = self.B
        xTarget = target.x
        yTarget = target.y
        t = target.t

        A = []
        for i in range(len(B)):
            A.append(0)

        A[0] = 0 

        num = xTarget**2 + (yTarget-B[0])**2 + B[3]**2 - 2*B[3] * (xTarget*sin(t) + (yTarget-B[0])*cos(t)) - B[1]**2 - B[2]**2  
        den = 2*B[1]*B[2]
        r = num/den

        A[2] = acos(r)

        K = B[1] + B[2]*r 
        num = K*(-B[0] + yTarget - B[3]*cos(t)) + B[2]*sin(A[2])*(xTarget-B[3]*sin(t)) 
        den = K**2 + (B[2]**2)*(1-cos(A[2])**2)  
        r = num/den

        A[1] = acos(r)

        A[3] = t - A[0] - A[1] - A[2]

        self.A = A
        return A

    def moovePinceToCoordonate(self,start,end,animation = False):
        """
        Approche le bras robotique vers un objet.
        Paramètres :
        - target : les coordonnées de l'objet.
        - animation : True pour afficher l'animation.
        """
        
        # Start and end position
        xStart = start[0]
        yStart = start[1]
        xEnd = end[0]
        yEnd = end[1]

        while xStart != xEnd and yStart != yEnd:

            if xStart > xEnd:
                while xStart > xEnd:
                    xStart -= 1

            elif xStart < xEnd:
                while xStart < xEnd:
                    xStart += 1

            if yStart > yEnd:
                while yStart > yEnd:
                    yStart -= 1

            elif yStart < yEnd:
                while yStart < yEnd:
                    yStart += 1
  
            target = Target(xStart,yStart,0)
            A = self.calculAngle(target)
            self.goToPosition(A,animation)
    

    def goToPosition(self,A,animation = False):
        """
        Met le bras dans la position décrite par la liste d'angles A.
        """
        self.A = A
        if animation == True:
            self.show()

# --- Fonctions ---

def degreeToRadian(A):
    """ Convertit les angles en degrés en radians. """
    for i in range(len(A)):
        A[i] = radians(A[i])
    return A

def demo1(bras,target):
    
    bras.calulAngle(target)
    bras.goToPosition(bras.A,True)
    
    target.x = bras.Sx[-1]

    while target.x < bras.xRangeMax:
        target.x += 1
        bras.calculAngle(target)
        bras.goToPosition(bras.A,True)

    while target.x > bras.xRangeMin:
        target.x -= 1
        bras.calculAngle(target)
        bras.goToPosition(bras.A,True)

def simulateur():
    
    # --- Paramètres objets ---
    
    arm = RobotArm([0, 45, 45, 45],[50, 80, 60, 20])
    target = Target(15,0,3/4*pi)

    # ---- Paramètres simulateur ---
    
    axeXMin = - 10
    axeYMin = - 10
    AxeXMax = arm.xRangeMax + 10
    axeYMax = arm.yRangeMax + 10

    # --- Initialisation de la fenêtre graphique ---

    plt.figure()

    # --- Choix de la simulation ---

    isEnd = False
    
    while isEnd == False:
        
        print("\nAffichage des segments du bras robot : ")

        print("\n0. pour des angles par défaut."
              "\n1. pour la pince sur un objet à une distance x,y donnée."
              "\n2. pour la pince sur un objet à une distance x variant entre xmin et xmax."
              "\n3. pour aller attraper un objet depuis angle par défaut."
              "\n4. Quitter.")
        
        choix = askFor.ABoundedNumber("Choix : ", 0, 4)

        if choix == 0:
            arm.show()
            arm.showAngles()
        
        elif choix == 1:
            target.x = askFor.ABoundedNumber("x : ", arm.xRangeMin, arm.xRangeMax)
            target.y = askFor.ABoundedNumber("y : ", arm.yRangeMin, arm.yRangeMax)
            arm.calculAngle(target)
            arm.goToPosition(arm.A)
            #target.show()

        elif choix == 2:
            target.y = 0
            target.x = 30
            demo1(arm,target)

        elif choix == 3:
            arm.goToPosition([0,0,0,0],True)
            target.x = arm.Sx[-1]
            target.y = arm.Sy[-1]
            arm.moovePinceToCoordonate(target,True)
            target.show()

        elif choix == 4: 
            isEnd = True 

simulateur()