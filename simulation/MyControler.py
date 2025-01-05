from time import sleep
import pygame
import MyDisplay
import MyCom


def connectControler():
    """Connecte la manette Xbox au programme."""

    # Initialiser pygame pour la manette.
    pygame.init()
    pygame.joystick.init()

    try:
        # Initialiser la manette.
        joystick = pygame.joystick.Joystick(0)  # Utiliser la première manette détectée
        joystick.init()
        print("Detected joystick "), joystick.get_name(), "'"
        return joystick

    except:
        print("Aucune manette détectée, retour")
        return None


def testXboxControler():
    """Teste la manette Xbox."""

    # Connecter une manette Xbox.
    joystick = connectControler()

    if joystick is None:
        return

    # Tester la manette.
    end = False
    while not end:
        pygame.event.pump()  # Keep the OS happy
        for event in pygame.event.get():
            print(event)


def controlArmInSimulationWithXboxControler(myArm):
    """Pilote le bras en simulation avec une manette Xbox."""

    joystick = connectControler()

    if joystick is None:
        return

    x1, y1 = (75, 75)
    x2, y2 = (75, 75)
    t = 3 / 4 * 3.14

    myArm.calculAngle([x1, y1], t)  # Calcul des angles pour atteindre le point x,y
    myArm.calculCoordonne()  # Calcul des coordonnées des points du bras pour pouvoir les afficher

    pause = 0.01

    MyDisplay.createWindow((6, 6))
    MyDisplay.showArmInWindow(myArm)

    try:
        end = False
        while not end:

            pygame.event.pump()  # Keep the OS happy

            for event in pygame.event.get():

                if event.type == pygame.JOYBUTTONDOWN:

                    # Arrêt si le bouton B est pressé.
                    if joystick.get_button(1):
                        print("Bouton B pressé, fin du controle du bras en simulation")
                        end = True

                    # On change angle d'approche si RB ou LB est pressé.
                    # <Event(1539-JoyButtonDown {'joy': 0, 'instance_id': 1, 'button': 4})>
                    while joystick.get_button(4):
                        t += 0.1
                        myArm.calculAngle([x1, y1], t)
                        myArm.calculCoordonne()
                        MyDisplay.showArmInWindow(myArm)
                        sleep(pause)
                    while joystick.get_button(5):
                        t -= 0.1
                        myArm.calculAngle([x1, y1], t)
                        myArm.calculCoordonne()
                        MyDisplay.showArmInWindow(myArm)
                        sleep(pause)

                # <Event(1538-JoyHatMotion {'joy': 0, 'instance_id': 1, 'hat': 0, 'value': (0, -1)})>
                # Bouge la position x,y de la pince en fonction de la croix directionnelle.
                # Tant que flèche directionnelle est pressée, bouger la pince.

                if event.type == pygame.JOYHATMOTION:
                    if joystick.get_hat(0)[0] == 1:
                        while joystick.get_hat(0)[0] != 0:
                            x2 = x1 + 5
                            myArm.moovePinceToCoordonate([x1, y1], [x2, y2], True, t)
                            x1 = x2
                            sleep(pause)

                    elif joystick.get_hat(0)[0] == -1:
                        while joystick.get_hat(0)[0] != 0:
                            x2 = x1 - 5
                            myArm.moovePinceToCoordonate([x1, y1], [x2, y2], True, t)
                            x1 = x2
                            sleep(pause)

                    elif joystick.get_hat(0)[1] == 1:
                        while joystick.get_hat(0)[1] != 0:
                            y2 = y1 + 5
                            myArm.moovePinceToCoordonate([x1, y1], [x2, y2], True, t)
                            y1 = y2
                            sleep(pause)

                    elif joystick.get_hat(0)[1] == -1:
                        while joystick.get_hat(0)[1] != 0:
                            y2 = y1 - 5
                            myArm.moovePinceToCoordonate([x1, y1], [x2, y2], True, t)
                            y1 = y2
                            sleep(pause)

    except KeyboardInterrupt:
        print("Arrêt du programme")
    finally:
        pygame.quit()
        MyDisplay.closeWindow()


def controlArmWithXboxControler(myArm):
    """
    Envoit des consgines au bras.
    format de la consigne : "x,y,t"
    """

    # On connecte la manette Xbox
    joystick = connectControler()

    # On initialise la position du bras
    x1, y1 = (75, 75)
    x2, y2 = (75, 75)
    t = 3 / 4 * 3.14
    pause = 0.01
    myArm.calculAngle([x1, y1], t)  # Calcul des angles pour atteindre le point x,y
    myArm.calculCoordonne()  # Calcul des coordonnées des points du bras pour pouvoir les afficher

    # Initialiser la simulation
    MyDisplay.createWindow((6, 6))  # Création d'une fenêtre d'un certaine taille
    MyDisplay.showArmInWindow(myArm)  # Affichage des segments du bras

    # Configurer la connexion série avec l'Arduino
    arduino = MyCom.initComWithArudino()

    try:
        end = False
        while not end:

            pygame.event.pump()  # Keep the OS happy

            for event in pygame.event.get():

                if event.type == pygame.JOYBUTTONDOWN:

                    # Arrêt si le bouton B est pressé.
                    if joystick.get_button(1):
                        print("Bouton B pressé, fin du controle du bras en simulation")
                        end = True

                    # On change angle d'approche si RB ou LB est pressé.
                    # <Event(1539-JoyButtonDown {'joy': 0, 'instance_id': 1, 'button': 4})>
                    while joystick.get_button(4):
                        t += 0.1
                        myArm.calculAngle([x1, y1], t)
                        myArm.calculCoordonne()
                        MyDisplay.showArmInWindow(myArm)
                        MyCom.sendToArduino(arduino, x1, y1, t)
                        sleep(pause)

                    while joystick.get_button(5):
                        t -= 0.1
                        myArm.calculAngle([x1, y1], t)
                        myArm.calculCoordonne()
                        MyDisplay.showArmInWindow(myArm)
                        MyCom.sendToArduino(arduino, x1, y1, t)
                        sleep(pause)

                # <Event(1538-JoyHatMotion {'joy': 0, 'instance_id': 1, 'hat': 0, 'value': (0, -1)})>
                # Bouge la position x,y de la pince en fonction de la croix directionnelle.
                # Tant que flèche directionnelle est pressée, bouger la pince.

                if event.type == pygame.JOYHATMOTION:
                    if joystick.get_hat(0)[0] == 1:
                        while joystick.get_hat(0)[0] != 0:
                            x2 = x1 + 5
                            myArm.moovePinceToCoordonate([x1, y1], [x2, y2], True, t)
                            x1 = x2
                            MyCom.sendToArduino(arduino, x1, y1, t)
                            sleep(pause)

                    elif joystick.get_hat(0)[0] == -1:
                        while joystick.get_hat(0)[0] != 0:
                            x2 = x1 - 5
                            myArm.moovePinceToCoordonate([x1, y1], [x2, y2], True, t)
                            x1 = x2
                            MyCom.sendToArduino(arduino, x1, y1, t)
                            sleep(pause)

                    elif joystick.get_hat(0)[1] == 1:
                        while joystick.get_hat(0)[1] != 0:
                            y2 = y1 + 5
                            myArm.moovePinceToCoordonate([x1, y1], [x2, y2], True, t)
                            y1 = y2
                            MyCom.sendToArduino(arduino, x1, y1, t)
                            sleep(pause)

                    elif joystick.get_hat(0)[1] == -1:
                        while joystick.get_hat(0)[1] != 0:
                            y2 = y1 - 5
                            myArm.moovePinceToCoordonate([x1, y1], [x2, y2], True, t)
                            y1 = y2
                            MyCom.sendToArduino(arduino, x1, y1, t)
                            sleep(pause)

    except KeyboardInterrupt:
        print("Arrêt du programme")
    finally:
        pygame.quit()
        MyDisplay.closeWindow()
        MyCom.closeComWihArduino(arduino)
