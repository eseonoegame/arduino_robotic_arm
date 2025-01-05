# arduino_robotic_arm

## Présentation rapide
Projet arduino pour un bras robotique. 
Le projet se décompose en 2 parties : 
- La partie arduino : bras robotique imprimé en 3D, articulé par des servosmoteurs, piloté par une carte arduino et joysticks.
- La partie simulation : simulation du bras robotique dans un environnement 2D avec python pour vérifier les équations qui permettebt au bras d'attrapper un objet tout seul, en connaissant juste sa position.

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