#include "MyServo.h" // On inclut le fichier d'en-tête de la classe MyServo

MyServo::MyServo(int pin, int angleInitial) // Constructeur de la classe MyServo
{
    pinServo = pin;         // On initialise le pin des servo moteurs à 0
    angle = angleInitial;   // On initialise l'angle initial des servo moteurs
    servo = Servo();        // On crée un objet de la classe Servo pour chaque servo moteur
    servo.attach(pinServo); // On attache chaque servo moteur à son pin
}

void MyServo::SetPosition(int consigne) // Fonction pour asservir les servo moteurs à un certain angle.
{
    if (consigne > 0 && consigne < 180) // On vérifie que l'angle donné est dans la plage de fonctionneent des servo moteurs.
    {
        // servo.attach(getPin()); // On attache le servo moteur à son pin
        servo.write(consigne); // On asservit le servo moteur à un angle donné
        angle = consigne;      // On met à jour l'angle du servo moteur
        lastActiveTime = millis();
    }
}

void MyServo::SetPlus()
{
    if (angle < 180 - PAS) // Si l'angle du servo moteur est inférieur à 180 degrés
    {
        // servo.attach(pinServo);
        angle = angle + PAS; // On incrémente l'angle de PAS degré
        servo.write(angle);  // On asservit le servo moteur à l'angle donné
        lastActiveTime = millis();
    }
}

void MyServo::SetMoins()
{
    if (angle > 0 + PAS) // Si l'angle du servo moteur est supérieur à 0 degrés
    {
        // servo.attach(pinServo);
        angle = angle - PAS; // On décrémente l'angle de PAS degré
        servo.write(angle);  // On asservit le servo moteur à l'angle donné
        lastActiveTime = millis();
    }
}

void MyServo::testServo(int pas, int pause) // Fonction pour tester le servo moteur
{
    // boucle de 0 à 180 degrés
    for (int i = angle; i <= 180; i += pas)
    {
        SetPosition(i); // On asservit le servo moteur à un angle donné
        delay(pause);   // On attend la durée spécifiée par 'pause'
    }
    // boucle de 180 à 0 degrés
    for (int i = 180; i >= 0; i -= pas)
    {
        SetPosition(i); // On asservit le servo moteur à un angle donné
        delay(pause);   // On attend la durée spécifiée par 'pause'
    }
}

int MyServo::getAngle() const // Fonction pour obtenir l'angle actuel des servo moteurs
{
    return angle; // On retourne l'angle actuel des servo moteurs
}

int MyServo::getPas() const // Fonction pour obtenir le pas des servo moteurs
{
    return PAS; // On retourne le pas des servo moteurs
}

int MyServo::getPin() const // Fonction pour obtenir le pin des servo moteurs
{
    return pinServo; // On retourne le pin des servo moteurs
}

void MyServo::detach() // Fonction pour détacher le servo moteur de son pin
{
    servo.detach(); // On détache le servo moteur de son pin
}