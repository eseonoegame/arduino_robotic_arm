"""
Simulateur du bras robotique.
Objectif : trouver les angles des servomoteurs pour atteindre un objet à une distance x,y et la pince du bras dans un angle t.
"""

import askFor as askFor
import console as console
import matplotlib.pyplot as plt
from math import *

def degreeToRadian(A):
    """ Convertit les angles en degrés en radians. """
    for i in range(len(A)):
        A[i] = radians(A[i])
    return A


def calculCoordonne(B, A):
    """ Calcule les coordonnées des points du bras robot. """

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


def calculAngle(B, x, y, t):
    """ Calcule les angles du bras robot. """
    
    A = []
    for i in range(len(B)):
        A.append(0)

    A[0] = 0 
    
    num = x**2 + (y-B[0])**2 + B[3]**2 - 2*B[3] * (x*sin(t) + (y-B[0])*cos(t)) - B[1]**2 - B[2]**2  
    den = 2*B[1]*B[2]
    r = num/den
    
    A[2] = acos(r)
    
    K = B[1] + B[2]*r 
    num = K*(-B[0] + y - B[3]*cos(t)) + B[2]*sin(A[2])*(x-B[3]*sin(t)) 
    den = K**2 + (B[2]**2)*(1-cos(A[2])**2)  
    r = num/den

    A[1] = acos(r)
    
    A[3] = t - A[0] - A[1] - A[2]
    
    return A


def AffichageAngles(A):
    """ Affiche les angles du bras robot. """
    liste = []
    largeur = 15

    for i in range(len(A)):
        liste.append([f"Angle {i} : ",f"{round(degrees(A[i]),3)} deg", f"{round(A[i],3)} rad"])
    
    print("\n" + largeur*3*"-")
    console.tabDisplay(liste, largeur)
    print(largeur*3*"-"+ "\n")


def affichageBras(Sx, Sy,xmin,ymin,xmax,ymax):
    """ Affiche les segments du bras robot. """
    plt.clf()
    plt.grid(True)
    plt.xlim(xmin, xmax)
    plt.ylim(ymin, ymax)
    for i in range(len(Sx)-1):
        plt.plot([Sx[i], Sx[i+1]], [Sy[i], Sy[i+1]], label=f"B{i}")
    plt.pause(0.05)
    plt.show()
 

def demonstration1(Sx, Sy, x, B, A, xmin, ymin, xmax, ymax, y, t, xMax, xMin):
    """ Animation du bras. """

    while x < xMax:
        x += 1
        A = calculAngle(B, x, y, t)  # Calculate new angles
        Sx, Sy = calculCoordonne(B, A)
        plt.clf()
        plt.grid(True)
        plt.axis('equal')
        plt.xlim(xmin, xmax)
        plt.ylim(ymin, ymax)
        for i in range(len(Sx)-1):
            plt.plot([Sx[i], Sx[i+1]], [Sy[i], Sy[i+1]], label=f"B{i}")
        plt.draw()
        plt.pause(0.05)
        
    while x > xMin:
        x -= 1
        A = calculAngle(B, x, y, t)  # Calculate new angles
        Sx, Sy = calculCoordonne(B, A)
        plt.clf()
        plt.grid(True)
        plt.axis('equal')
        plt.xlim(xmin, xmax)
        plt.ylim(ymin, ymax)
        for i in range(len(Sx)-1):
            plt.plot([Sx[i], Sx[i+1]], [Sy[i], Sy[i+1]], label=f"B{i}")
        plt.draw()
        plt.pause(0.05)

def GoTakeObject(Sx, Sy, x, B, A, AxeXMin, AxeYMin, AxeXMax, AxeYMax, y, t, xMax, xMin):
    """Approche du bras robotique vers l'objet."""
    
    # 1. On affiche les segments du bras robot avec les angles par défaut.
    # 2. On demande à l'utilisateur de saisir les coordonnées de l'objet.
    # 3. On calcule les angles pour atteindre l'objet.
    # 4. On affiche le bras qui tend progressivement vers la position de l'objet.
    
    # 1. On affiche les segments du bras robot avec les angles par défaut.

    Sx,Sy = calculCoordonne(B, A)
    plt.clf()
    plt.grid(True)
    plt.xlim(AxeXMin, AxeXMax)
    plt.ylim(AxeYMin, AxeYMax)
    for i in range(len(Sx)-1):
        plt.plot([Sx[i], Sx[i+1]], [Sy[i], Sy[i+1]], label=f"B{i}")
    plt.pause(0.05)
    plt.draw()

    # 2. On demande à l'utilisateur de saisir les coordonnées de l'objet.

    xTarget = askFor.ABoundedNumber("Distance de l'objet : ", xMin, xMax)
    yTarget = askFor.ABoundedNumber("Hauteur de l'objet : ",0,100)
    tTarget = askFor.ABoundedNumber("Angle d'approche : ",0,2*pi)

    xPince = Sx[-1]
    yPince = Sy[-1]
    tPince = t

    print(f"\nPosition actuelle de la pince : ({xPince},{yPince},{tPince})")
    print(f"Position de l'objet : ({xTarget},{yTarget},{tTarget})")

    # 3. On calcule les angles pour atteindre l'objet.
    # 4. On affiche le bras qui tend progressivement vers la position de l'objet.

    while xPince < xTarget:
        x += 1
        while yPince < yTarget:
            y += 1
            while tPince < tTarget:
                t += 0.1
                
                A = calculAngle(B, x, y, t)
                Sx, Sy = calculCoordonne(B, A)
                plt.clf()
                plt.grid(True)
                plt.axis('equal')
                plt.xlim(AxeXMin, AxeXMax)
                plt.ylim(AxeXMin, AxeYMax)
                for i in range(len(Sx)-1):
                    plt.plot([Sx[i], Sx[i+1]], [Sy[i], Sy[i+1]], label=f"B{i}")
                plt.draw()
                plt.pause(0.05)


def main():

    # --- Paramètres objet ---
    
    xTarget = 15        # distance de l'objet
    yTarget = 0         # hauteur de l'objet
    tTarget = 3/4*pi    # angle d'approche

    xTargetMax = 160
    xTargetMin = 30
    yTargetMax = 160
    yTargetMin = 0

    # --- Paramètres robot ---
    
    h = 60                # Hauteur du socle du bras
    B = [h, 100, 80, 20]  # B0,B1,B2,B3 (longueur des segments en mm)
    A = [0, 5, 175, 5]   # A0,A1,A2,A3 (angles entre les segments en degré)

    # ---- Paramètres simulateur ---

    axeXMin = -10
    axeYMin = -10
    AxeXMax = xTargetMax+10
    axeYMax = yTargetMax+10

    # --- Initialisation ---

    A = degreeToRadian(A)
    Sx = [0, 0, 0, 0, 0]
    Sy = [0, 0, 0, 0, 0]

    plt.figure(figsize=(10, 8))
    plt.clf()
    plt.grid(True)
    plt.axis('equal')
    plt.xlim(axeXMin, AxeXMax)
    plt.ylim(axeYMin, axeYMax)

    # --- Simulateur ---
      
    isEnd = False
    
    while isEnd == False:
        
        print("\nAffichage des segments du bras robot : "
              "\n0. pour des angles par défaut."
              "\n1. pour un objet à une distance x donnée."
              "\n2. pour un objet à une distance x variant entre xmin et xmax."
              "\n3. pour aller attraper un objet."
              "\n4. Quitter.")
        
        choix = askFor.ABoundedNumber("Choix : ", 0, 4)

        # On affiche les segments du bras robot avec les angles par défaut.
        if choix == 0:
            Sx,Sy = calculCoordonne(B, A)
            AffichageAngles(A)
            affichageBras(Sx, Sy,axeXMin,axeYMin,AxeXMax,axeYMax)
            
        # On affiche les segments du bras robot avec les angles calculés pour atteindre un objet à une distance x donnée.
        elif choix == 1:
            A = calculAngle(B, xTarget, yTarget, tTarget)
            Sx,Sy = calculCoordonne(B, A)
            affichageBras(Sx, Sy, axeXMin, axeYMin, AxeXMax, axeYMax)
            AffichageAngles(A)
        
        # On affiche les segments du bras robot avec les angles calculés pour atteindre un objet à une distance x variant entre xmin et xmax.
        elif choix == 2:
            demonstration1(Sx, Sy, xTarget, B, A, axeXMin, axeYMin, AxeXMax, axeYMax, yTarget, tTarget, xTargetMax, xTargetMin)
        
        # On affiche les segments du bras robot avec les angles qui varient.
        elif choix == 3:
            Sx,Sy = calculCoordonne(B, A)
            GoTakeObject(Sx, Sy, xTarget, B, A, axeXMin, axeYMin, AxeXMax, axeYMax, yTarget, tTarget, xTargetMax, xTargetMin)

        else :
            isEnd = True
            print("Au revoir !")
    
main()