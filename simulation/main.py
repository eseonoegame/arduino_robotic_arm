import matplotlib.pyplot as plt
from math import *
import askFor as askFor

def calculCoordonne(Sx, Sy, B, a, h, x):
    """ Calcule les coordonnées des points du bras robot. """
    Sx[0] = 0
    Sy[0] = 0
    
    Sx[1] = 0
    Sy[1] = h

    Sx[2] = Sx[1] + B[1]*sin(a[0])
    Sy[2] = Sy[1] + B[1]*cos(a[0])

    Sx[3] = Sx[2] + B[2]*sin(a[0]+a[1])
    Sy[3] = Sy[2] + B[2]*cos(a[0]+a[1])

    Sx[4] = Sx[3] + B[3]*sin(a[0]+a[1]+a[2])
    Sy[4] = Sy[3] + B[3]*cos(a[0]+a[1]+a[2])

    return Sx, Sy

def calculAngle(a, x, y, B, theta,h):
    """ Calcule les angles du bras robot. """
    
    a[0] = acos( (y-B[2*cos(theta)]-h) / B[0]+B[1]*cos(a[1]) + sin(a[1]) * (B[1]*x-B[2]*sin(theta)) / (B[0]+B[1]*cos(a[1])) )
    
    a[1] = acos( (x**2+(y-h)**2+B[2]**2-2*B[2*(x*sin(theta)+(y-h)*cos(theta))]) - (B[0]**2 - B[1]**2 ) / (2*B[0]*B[1]) )
    
    a[2] = theta - a[0]-a[1]
    
    return a

def AffichageAngles(A):
    """ Affiche les angles du bras robot. """
    print("\n" + 40*"-")
    for i in range(len(A)):
        print(f"Angle {i} : {round(A[i],4)} radian | {round(degrees(A[i]),4)} degré")
    print(40*"-"+ "\n")

def affichageBras(listeSx, listeSy):
    """ Affiche les segments du bras robot. """
    plt.clf()
    for i in range(len(listeSx)-1):
        plt.plot([listeSx[i], listeSx[i+1]], [listeSy[i], listeSy[i+1]], label=f"B{i}")
 
    plt.grid(True)
    plt.axis('equal')
    plt.xlim(-10, 200)
    plt.ylim(-10, 300)

def demonstration1(Sx, Sy, x, h, B, a):
    xmax = 10
    xmin = 1
    plt.show
    while True:
        while x < xmax:
            x += 0.01
            Sx, Sy = calculCoordonne(Sx, Sy, x, h, B, a)
            plt.pause(0.05)
            plt.clf()
            affichageBras(Sx, Sy)
        while x > xmin:
            x-=0.01
            Sx, Sy = calculCoordonne(Sx, Sy, x, h, B, a)
            plt.pause(0.05)
            affichageBras(Sx, Sy)

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
        Sx, Sy = calculCoordonne(Sx, Sy, x, h, B, angles)
        affichageBras(Sx, Sy)
        plt.pause(0.05)

def degreeToRadian(A):
    """ Convertit les angles en degrés en radians. """
    for i in range(len(A)):
        A[i] = radians(A[i])
    return A

def main():

    # --- Paramètres du robot ---
    # unité : mm et degré

    x = 150
    h = 60

    B = [h, 100, 100, 60]
    A = [45, 45, 45]
    Sx = [0, 0, 0, 0, 0]
    Sy = [0, h, 0, 0, 0]

    theta =  A[0] + A[1] + A[2]
    y = 0

    # --- Initialisation ---

    A = degreeToRadian(A)
    
    # --- Affichage ---
    # Choisir l'affichage souhaité
    
    isEnd = False
    while isEnd == False:
        print("\nAffichage des segments du bras robot : "
              "\n0. pour des angles à 45 degrés."
              "\n1. pour un objet à une distance x donnée."
              "\n2. pour un objet à une distance x variant entrexmin et xmax."
              "\n3. avec des angles qui varient."
              "\n4. Quitter.")
        choix = askFor.ABoundedNumber("Choix : ", 0, 4)

        if choix == 0:
            Sx,Sy = calculCoordonne(Sx, Sy, B, A, h, x)
            affichageBras(Sx, Sy)
            AffichageAngles(A)
            plt.show()

        elif choix == 1:
            A = calculAngle(A, x, y, B, theta, h)
            Sx,Sy = calculCoordonne(Sx, Sy, B, A, h, x)
            affichageBras(Sx, Sy)
            AffichageAngles(A)
            plt.show() # Affiche la figure à l'écran

        elif choix == 2:
            demonstration1(Sx, Sy)
            plt.show() # Affiche la figure à l'écran
        
        elif choix == 3:
            demonstration2(Sx, Sy)
            plt.show() # Affiche la figure à l'écran

        else :
            isEnd = True
            print("Au revoir !")
    
main()