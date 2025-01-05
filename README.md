# arduino_robotic_arm

## Présentation rapide

Projet : bras robotique arduino. 
Objectif : Avoir un bras robotique qui peut :
- être piloté par des joysticks (en angle ou en position de la pince)
- être piloté par une manette XBOX (en angle ou en position de la pince)
- attraper un objet tout seul, en connaissant juste sa position

Le code du projet se décompose en 2 parties : 
- La partie arduino : 
    - Le code pour piloter le bras robotique avec les joystick
    - Le code pour faire les maths pour pouvoir piloter la position de la pince du bras robotique 

- La partie python :
    - Le code pour simuler mathématiquement le bras robotique
    - Le code pour afficher la simulation du bras robotique
    - Le code pour récupérer les inputs de la manette XBOX
    - Le code pour gérer la communication entre le PC et l'arduino
    
## Décomposition du code

### Partie arduino
- `main.ino` : code arduino pour piloter le bras robotique
- `MyServo.cpp` : classe pour gérer les servos moteurs
- `MyJoystick.cpp` : classe pour gérer les joysticks
- `MyCom.cpp` : classe pour gérer la communication entre l'arduino et le PC
- `MyOperatingMode.cpp` : Les différentes fonctions qui permettent de piloter le bras robotique de plusieurs manières possibles
- `MyMath.cpp` : Les fonctions mathématiques pour calculer les angles des servos moteurs

### Partie simulation
- `main.py` : code python pour simuler le bras robotique
- `MyMath.py` : Les fonctions mathématiques pour calculer les angles des servos moteurs
- `MyController` : réucpère les inputs de la manette XBOX
- `MyVirtualArm.py` : classe pour gérer le bras robotique
- `MyDisplay.py` : code pour afficher la simulation du bras robot
- `MyCom.py` : code pour gérer la communication entre le PC et l'arduino
- `MyDraw.py` : code pour dessiner avec le bras robotique

## Matériel

- 1x Arduino Uno
- 6x Servomoteurs MG996R
- 2x Joysticks
- 1x Manette XBOX
- 1x capteur ultrason