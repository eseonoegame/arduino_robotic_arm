#include "MyJoystick.h"

MyJoystick::MyJoystick(int pinAxeX, int pinAxeY, int bp) // Constructeur de la classe MyServo
{
    PIN_AXE_X = pinAxeX; // On initialise le pin de l'axe X
    PIN_AXE_Y = pinAxeY; // On initialise le pin de l'axe Y
    PIN_BP = bp;         // On initialise le pin du bouton poussoir

    pinMode(PIN_AXE_X, INPUT); // définition du pin comme une entrée
    pinMode(PIN_AXE_Y, INPUT);
    pinMode(PIN_BP, INPUT);
    digitalWrite(PIN_BP, HIGH); // Activation de la résistance de Pull-Up interne de la carte Uno
}

void MyJoystick::getValues() // Fonction pour réupérer les valeurs des joysticks
{
    xValue = analogRead(PIN_AXE_X);
    yValue = analogRead(PIN_AXE_Y);
    BPValue = digitalRead(PIN_BP);
    rawValues[0] = xValue;
    rawValues[1] = yValue;
    rawValues[2] = BPValue;
}

void MyJoystick::testJoystick() // Fonction pour tester le joystick
{
    getValues();
    Serial.print("xValue = ");
    Serial.print(xValue);
    Serial.print(" yValue = ");
    Serial.print(yValue);
    Serial.print(" BPValue = ");
    Serial.println(BPValue);
}

// Méthodes pour obtenir les valeurs des axes et du bouton
int MyJoystick::getXValue() const // const pour dire que la fonction ne modifie pas la valeur.
{
    return xValue;
}

int MyJoystick::getYValue() const
{
    return yValue;
}

int MyJoystick::getBPValue() const
{
    return BPValue;
}

int *MyJoystick::getRawValues() const
{
    return (int *)rawValues;
}