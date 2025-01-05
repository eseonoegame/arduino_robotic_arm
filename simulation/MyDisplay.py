import matplotlib.pyplot as plt


def createWindow(size):
    """Crée une fenêtre graphique."""
    plt.figure(figsize=size)


def closeWindow():
    """Ferme la fenêtre graphique."""
    plt.close()


def showArmInWindow(myArm):
    """Dessine le bras robotique."""

    plt.pause(0.05)
    plt.clf()
    plt.grid(True)
    plt.axis("equal")
    plt.title("Bras robotique")
    plt.xlabel("x")
    plt.ylabel("y")

    # On définit les limites de l'affichage.
    # On est dans une fenêtre carré (plt.figure(figsize=(9, 9))) donc on doit mettre les mêmes limites pour x et y sinon il y a des problèmes d'affichage.
    plt.xlim(-10, 180)
    plt.ylim(-10, 180)

    # On affiche chaque segment du bras.
    for i in range(len(myArm.Sx) - 1):
        plt.plot(
            [myArm.Sx[i], myArm.Sx[i + 1]],
            [myArm.Sy[i], myArm.Sy[i + 1]],
            label=f"B{i}",
            linewidth=3,
        )

    plt.tight_layout()
    plt.draw()
