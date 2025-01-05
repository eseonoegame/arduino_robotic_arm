import serial
import time


def initComWithArudino():
    """Initialise la connexion série avec l'Arduino."""

    # Configurer la connexion série avec l'Arduino
    try:
        arduino = serial.Serial("COM3", 9600, timeout=2)
        time.sleep(2)  # Attendre la connexion série
        return arduino
    except serial.SerialException as e:
        print(f"Erreur de connexion : {e}")
        return None


def sendToArduino(arduino, x, y, t):
    """Envoie les données x, y et t à l'Arduino."""
    if not arduino or not arduino.is_open:
        print("Erreur: Port série non ouvert")
        return False
    try:
        # Construire une chaîne de données
        data = f"{x:.2f},{y:.2f},{t:.2f}\n"  # Exemple de format : "0.12,-0.45\n"

        # Envoyer les données à l'Arduino
        arduino.write(data.encode("utf-8"))

        # Afficher les données envoyées pour débogage
        print(f"Envoyé : {data}")
        time.sleep(0.1)
        return True

    except Exception as e:
        print(f"Erreur d'envoi: {e}")
        return False


def closeComWihArduino(arduino):
    """Ferme la connexion série avec l'Arduino."""
    if arduino.is_open:
        arduino.close()
