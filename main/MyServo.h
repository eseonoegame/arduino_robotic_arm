#include <Arduino.h>
#include <Servo.h> // On inclut la librairie Servo pour pouvoir utiliser les fonctions de la classe Servo

#ifndef MyServo_h
#define MyServo_h

class MyServo
{
public:
    MyServo(int pin, int angle);        // Constructeur de la classe MyServo
    void SetPosition(int position);     // Fonction pour asservir les servo moteurs à un certain angle.
    void SetPlus();                     // Fonction pour augmenter l'angle des servo moteurs
    void SetMoins();                    // Fonction pour diminuer l'angle des servo moteurs
    void testServo(int pas, int pause); // Fonction pour tester le servo moteur
    void detach();                      // Fonction pour détacher le servo moteur de son pin

    int getAngle() const; // Fonction pour obtenir l'angle actuel des servo moteurs
    int getPas() const;   // Fonction pour obtenir le pas des servo moteurs
    int getPin() const;   // Fonction pour obtenir le pin des servo moteurs

private:
    Servo servo;                  // On crée un objet de la classe Servo pour chaque servo moteur
    int pinServo;                 // On garde le pin de chaque servo moteur dans une variable
    int angle;                    // On garde l'angle des servo moteurs dans une variable
    int PAS = 3;                  // On définit de combien le servo moteur va bouger à chaque incrémentation/décrémentation
    unsigned long lastActiveTime; // On garde le temps de la dernière action sur le servo moteur
};

#endif
