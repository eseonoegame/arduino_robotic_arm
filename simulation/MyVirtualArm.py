from math import sin, cos, acos, degrees, radians, pi
import console as console
import matplotlib.pyplot as plt

def degreeToRadian(liste):
    """ Convertit une liste d'angles en degrés en une liste d'angles en radians. """
    for i in range(len(liste)):
        liste[i] = radians(liste[i])
    return liste

class MyVirtualArm :
    def __init__(self,A,B):
        """ 
        Angle par défaut du bras robot. 
        Longueur des segments du bras robot.
        """
        self.A = A
        self.B = B

        self.xRangeMax = sum(B)-B[0]
        self.xRangeMin = 0
        self.yRangeMax = B[0] + B[1] -30
        self.yRangeMin = 0

        self.A = degreeToRadian(A)
        self.Sx = [0, 0, 0, 0, 0]
        self.Sy = [0, 0, 0, 0, 0]

    def __str__(self):
        """ Affiche les longueurs des segments et les angles du bras.
        """
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

        plt.pause(0.05)
        plt.clf()
        plt.grid(True)
        plt.axis('equal')
        plt.title("Bras robotique")
        plt.xlabel("x")
        plt.ylabel("y")

        # On définit les limites de l'affichage.
        # On est dans une fenêtre carré (plt.figure(figsize=(9, 9))) donc on doit mettre les mêmes limites pour x et y sinon il y a des problèmes d'affichage.
        plt.xlim(-10,180)
        plt.ylim(-10,180)
        
        # On affiche chaque segment du bras.
        for i in range(len(self.Sx)-1):
            plt.plot([self.Sx[i], self.Sx[i+1]], [self.Sy[i], self.Sy[i+1]], label=f"B{i}",linewidth=3)
        
        plt.tight_layout()
        plt.draw()

        def showWithTrace(self):
            """Dessine le bras robot avec des points pour chaque position de la pince."""
            plt.pause(0.05)
            plt.clf()
            plt.grid(True)
            plt.axis('equal')
            plt.title("Bras robotique")
            plt.xlabel("x")
            plt.ylabel("y")

            # On définit les limites de l'affichage.
            # On est dans une fenêtre carré (plt.figure(figsize=(9, 9))) donc on doit mettre les mêmes limites pour x et y sinon il y a des problèmes d'affichage.
            plt.xlim(-10,180)
            plt.ylim(-10,180)
            
            # On affiche chaque segment du bras.
            for i in range(len(self.Sx)-1):
                plt.plot([self.Sx[i], self.Sx[i+1]], [self.Sy[i], self.Sy[i+1]], label=f"B{i}",linewidth=3)
            
            # On affiche les points de la pince.
            plt.plot(self.Sx[-1], self.Sy[-1], 'ro', label="Pince")
            plt.tight_layout()
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

        self.Sx = Sx
        self.Sy = Sy
        return Sx, Sy

    def calculAngle(self, target, t=3/4*pi):
        """ 
        Calcule les angles du bras robot pour atteindre un point (x,y) avec une pince dans un angle t. 
        """

        B = self.B
        x = target[0]
        y = target[1]

        A = []
        for i in range(len(B)):
            A.append(0)

        # --- maths comliquées ---

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

        self.A = A
        return A

    def moovePinceToCoordonate(self,start,end,animation = False, t= None):
        """
        Déplace la pince du bras robotique d'une position start (x,y) à une position end (x,y). 
        """    

        if animation:        
            x = start[0]
            y = start[1]
            xEnd = end[0]
            yEnd = end[1]

            # On calcul et affiche la position du bras jusqu'à atteindre la position finale.
            while x != xEnd or y != yEnd:

                if x < xEnd :
                    x += 1
                elif x > xEnd :
                    x -= 1
                else :
                    # On ne bouge pas en x
                    pass
                if y < yEnd :
                    y += 1
                elif y > yEnd :
                    y -= 1
                else :
                    # On ne bouge pas en y
                    pass
                 
                self.calculAngle([x,y],t)
                self.calculCoordonne()
                self.show()
                #print(f"debug {self.Sx[-1]} {self.Sy[-1]}")

        # Si pas d'animation alors on calcul que la position finale.
        else :
            self.calculAngle(end)
            self.calculCoordonne()
            self.show([start[0],end[0]],[start[1],end[1]])
