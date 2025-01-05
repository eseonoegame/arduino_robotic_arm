import MyDisplay as MyDisplay
from math import cos, sin


def drawASquare(myArm):
    # Dessiner un carré.
    MyDisplay.createWindow((6, 6))
    x1 = 75
    y1 = 50

    x2 = 125
    y2 = 50

    x3 = 125
    y3 = 100

    x4 = 75
    y4 = 100

    myArm.moovePinceToCoordonate([x1, y1], [x2, y2], True)
    myArm.moovePinceToCoordonate([x2, y2], [x3, y3], True)
    myArm.moovePinceToCoordonate([x3, y3], [x4, y4], True)
    myArm.moovePinceToCoordonate([x4, y4], [x1, y1], True)
    MyDisplay.closeWindow()


def drawATriangle(myArm):
    # Dessiner un triangle.
    MyDisplay.createWindow((6, 6))
    x1 = 50
    y1 = 50

    x2 = 100
    y2 = 50

    x3 = 100
    y3 = 100

    myArm.moovePinceToCoordonate([x1, y1], [x2, y2], True)
    myArm.moovePinceToCoordonate([x2, y2], [x3, y3], True)
    myArm.moovePinceToCoordonate([x3, y3], [x1, y1], True)
    MyDisplay.closeWindow()


def drawACircle(myArm):  # NE FONCTIONNE PAS
    # Dessiner un cercle.
    MyDisplay.createWindow((6, 6))
    x = 75
    y = 50
    r = 25
    for i in range(0, 618, 10):  # 628 = 2*pi*100
        i = i / 100
        x1 = round(x + r * cos(i))
        y1 = round(y + r * sin(i))
        x2 = round(x + r * cos(i + 0.1))
        y2 = round(y + r * sin(i + 0.1))
        myArm.moovePinceToCoordonate([x1, y1], [x2, y2], True)
    MyDisplay.closeWindow()


def drawAline(myArm, n):
    """dessine une ligne, en faisant n aller retour."""
    MyDisplay.createWindow((6, 6))
    for _ in range(2 * n):
        xStart = 50
        yStart = 0
        xEnd = 120
        yEnd = 0
        myArm.moovePinceToCoordonate([xStart, yStart], [xEnd, yEnd], True)
        myArm.moovePinceToCoordonate([xEnd, yEnd], [xStart, yStart], True)
    MyDisplay.closeWindow()
