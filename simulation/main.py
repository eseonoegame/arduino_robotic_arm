import matplotlib.pyplot as plt
from math import *

def calcul(Sx, Sy, x, h, B, a):
    """ Calcule les coordonnées des points du bras robot. """
    Sx[0] = 0
    Sy[0] = 0
    
    Sx[1] = 0
    Sy[1] = h

    Sx[2] = Sx[1] + B[1]*sin(radians(a[0]))
    Sy[2] = Sy[1] + B[1]*cos(radians(a[0]))
    
    Sx[3] = Sx[2] + B[2]*sin(radians(a[0]+a[1]))
    Sy[3] = Sy[2] + B[2]*cos(radians(a[0]+a[1]))
    
    Sx[4] = Sx[3] + B[3]*sin(radians(a[0]+a[1]+a[2]))
    Sy[4] = Sy[3] + B[3]*cos(radians(a[0]+a[1]+a[2]))

    """
    S0x = 0
    S0y = 0

    S1x = 0
    S1y = h

    S2x = B1*cos(radians(a1))
    S2y = h + B1*sin(radians(a1))

    S3x = B2*cos(radians(a1+a2))-B1*sin(radians(a1))
    S3y = B2*sin(radians(a1+a2))+B1*cos(radians(a1))+h
    """
    return Sx, Sy

def affichage(listeSx, listeSy):
    """ Affiche les segments du bras robot. """
    plt.clf()
    for i in range(len(listeSx)-1):
        plt.plot([listeSx[i], listeSx[i+1]], [listeSy[i], listeSy[i+1]], label=f"B{i}")
 
    plt.grid(True)
    plt.axis('equal')
    plt.xlim(-1, 15)
    plt.ylim(-1, 15)

def demonstration(Sx, Sy, x, h, B, a):
    xmax = 10
    xmin = 1
    plt.show
    while True:
        while x < xmax:
            x += 0.01
            calcul(Sx, Sy, x, h, B, a)
            plt.pause(0.05)
            plt.clf()
            affichage(Sx, Sy)
        while x > xmin:
            x-=0.01
            calcul(Sx, Sy, x, h, B, a)
            plt.pause(0.05)
            affichage(Sx, Sy)

def demonstration2(Sx, Sy, x, h, B, angles):
    """Animation des angles du bras."""
    plt.ion()  # Mode interactif
    while True:
        # Update angles
        for i in range(len(angles)):
            angles[i] += 1
            if angles[i] > 90:
                angles[i] = 0
                
        # Calculate and display
        Sx, Sy = calcul(Sx, Sy, x, h, B, angles)
        affichage(Sx, Sy)
        plt.pause(0.05)

def main():

    # --- Paramètres du robot ---
    x = 15
    h = 5
    B = [5, 5, 5, 5]
    a = [45, 45, 45, 45]
    Sx = [0, 0, 0, 0, 0]
    Sy = [0, h, 0, 0, 0]

    # --- Calcul des coordonnées des points ---
    
    calcul(Sx, Sy, x, h, B, a)
    
    # --- Paramètre d'affichage ---
    
    plt.figure()     
    plt.title('Bras robot')
    plt.grid(False)
    plt.xlim(-15, 15)
    plt.ylim(-15, 15)
    plt.axis('equal')

    # --- Affichage ---

    affichage(Sx, Sy)
    #demonstration(Sx, Sy, x, h, B, a)
    #demonstration2(Sx, Sy, x, h, B, a)
    plt.show() # Affiche la figure à l'écran


main()