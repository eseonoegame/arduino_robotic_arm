#include <Arduino.h>

#ifndef MyJoystick_h
#define MyJoystick_h

class MyJoystick
{
public:
    // Constructeur de la classe MyJoystick
    MyJoystick(int pinAxeX, int pinAxeY, int bp);

    // Fonction pour récupérer les valeurs des joysticks
    void getValues();

    // Fonction pour tester le joystick
    void testJoystick();

    // Fonctions pour obtenir les valeurs des axes et du bouton
    int getXValue() const;
    int getYValue() const;
    int getBPValue() const;
    int *getRawValues() const;

private:
    int PIN_AXE_X;    // Broche de l'axe X
    int PIN_AXE_Y;    // Broche de l'axe Y
    int PIN_BP;       // Broche du bouton poussoir
    int xValue;       // Valeur de l'axe X
    int yValue;       // Valeur de l'axe Y
    int BPValue;      // Valeur du bouton poussoir
    int rawValues[3]; // Tableau pour stocker les valeurs des axes et du bouton
};

#endif
