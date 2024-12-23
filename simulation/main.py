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
 

def demonstration1(Sx, Sy, x, B, A, xmin, ymin, xmax, ymax):
    """ Animation du bras. """
    while True:
        while x < xmax:
            x += 1
            Sx, Sy = calculCoordonne(B, A)
            affichageBras(Sx, Sy,xmin,ymin,xmax,ymax)
        while x > xmin:
            x-=1
            Sx, Sy = calculCoordonne(Sx, Sy, x, B, A)
            affichageBras(Sx, Sy,xmin,ymin,xmax,ymax)


def demonstration2(Sx, Sy, x, B, A, xmin, ymin, xmax, ymax):
    """Animation des angles du bras."""
    while True:

        for i in range(len(A)):
            A[i] += 1
            if A[i] > 90:
                A[i] = 0
                
        Sx, Sy = calculCoordonne(Sx, Sy, x, B, A)
        affichageBras(Sx, Sy,xmin,ymin,xmax,ymax)


def main():

    # --- Paramètres objet ---
    
    x = 15  # distance de l'objet
    y = 0   # hauteur de l'objet
    t = pi  # angle d'approche

    # --- Paramètres robot ---
    
    h = 60                # Hauteur du socle du bras
    B = [h, 100, 80, 20]  # B0,B1,B2,B3 (longueur des segments en mm)
    A = [0, 45, 45, 45]   # A0,A1,A2,A3 (angles entre les segments en degré)

    # ---- Paramètres simulateur ---

    xmin = -10
    ymin = -10
    xmax = sum(B)
    ymax = sum(B)

    # --- Initialisation ---

    A = degreeToRadian(A)
    Sx = [0, 0, 0, 0, 0]
    Sy = [0, 0, 0, 0, 0]

    plt.figure()
    plt.clf()
    plt.grid(True)
    plt.axis('equal')
    plt.xlim(xmin, xmax)
    plt.ylim(ymin, ymax)

    # --- Simulateur ---
      
    isEnd = False
    
    while isEnd == False:
        
        print("\nAffichage des segments du bras robot : "
              "\n0. pour des angles par défaut."
              "\n1. pour un objet à une distance x donnée."
              "\n2. pour un objet à une distance x variant entre xmin et xmax."
              "\n3. avec des angles qui varient."
              "\n4. Quitter.")
        
        choix = askFor.ABoundedNumber("Choix : ", 0, 4)

        # On affiche les segments du bras robot avec les angles par défaut.
        if choix == 0:
            Sx,Sy = calculCoordonne(B, A)
            AffichageAngles(A)
            affichageBras(Sx, Sy,xmin,ymin,xmax,ymax)
            
        # On affiche les segments du bras robot avec les angles calculés pour atteindre un objet à une distance x donnée.
        elif choix == 1:
            A = calculAngle(B, x, y, t)
            Sx,Sy = calculCoordonne(B, A)
            affichageBras(Sx, Sy, xmin, ymin, xmax, ymax)
            AffichageAngles(A)
        
        # On affiche les segments du bras robot avec les angles calculés pour atteindre un objet à une distance x variant entre xmin et xmax.
        elif choix == 2:
            demonstration1(Sx, Sy, x, B, A, xmin, ymin, xmax, ymax)
        
        # On affiche les segments du bras robot avec les angles qui varient.
        elif choix == 3:
            demonstration2(Sx, Sy, x, B, A, xmin, ymin, xmax, ymax)

        else :
            isEnd = True
            print("Au revoir !")
    
main()